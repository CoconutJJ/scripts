/*
PNG Tool

This PNG Tool can read a PNG, decompress the image data using zlib.
Author: David Yue
*/

#include "zconf.h"
#include "zlib.h"
#include <arpa/inet.h>
#include <assert.h>
#include <errno.h>
#include <fcntl.h>
#include <getopt.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/fcntl.h>
#include <sys/mman.h>
#include <unistd.h>
#define PNG_HEADER      "\211PNG\r\n\032\n"
#define IHDR_CHUNK_TYPE 0
#define IDAT_CHUNK_TYPE 1
#define PLTE_CHUNK_TYPE 2

#define FILTER_NONE  0
#define FILTER_SUB   1
#define FILTER_UP    2
#define FILTER_AVG   3
#define FILTER_PAETH 4

#define COLOR_TYPE_GRAYSCALE       0
#define COLOR_TYPE_RGB             2
#define COLOR_TYPE_PLTE            3
#define COLOR_TYPE_GRAYSCALE_ALPHA 4
#define COLOR_TYPE_RGBA            6

char *png_file_name = NULL;
struct __attribute__ ((__packed__)) zlib_format {
        uint8_t CM : 4;
        uint8_t CINFO : 4;
        uint8_t FCHECK : 5;
        uint8_t FDICT : 1;
        uint8_t FLEVEL : 2;
        uint32_t DICTID;
};

struct __attribute__ ((__packed__)) IHDRChunk {
        uint32_t length;
        char chunk_type[4];
        uint32_t width;
        uint32_t height;
        uint8_t bit_depth;
        uint8_t color_type;
        uint8_t compression_method;
        uint8_t filter_method;
        uint8_t interlace_method;
        uint32_t crc;
};

struct __attribute__ ((__packed__)) PNGChunkHeader {
        uint32_t length;
        char chunk_type[4];
        char data[];
};

struct __attribute__ ((__packed__)) PNG {
        char header[8];
        struct IHDRChunk ihdr_chunk;
        char data[];
};

struct ImageData {
        uint8_t *data;
        size_t width;
        size_t height;
        uint8_t bit_depth;
        uint8_t color_type;
};

void nputs (char *s, size_t n)
{
        while (n-- > 0) {
                putchar ((int)*s);
                s++;
        }
}

int read_chunk_type (const char chunk_type[4])
{
        char buf[4];

        for (int i = 0; i < 4; i++) {
                buf[i] = chunk_type[i] & ~(1 << 5);
        }

        if (strncmp ("IDAT", buf, 4) == 0) {
                return IDAT_CHUNK_TYPE;
        }

        if (strncmp ("PLTE", buf, 4) == 0) {
                return PLTE_CHUNK_TYPE;
        }

        if (strncmp ("IHDR", buf, 4) == 0) {
                return IHDR_CHUNK_TYPE;
        }
        return -1;
}

struct PNGChunkHeader *
iter_chunks (struct PNGChunkHeader *start_chunk, size_t *iter_bytes, struct PNGChunkHeader *end_ptr)
{
        struct PNGChunkHeader *curr_chunk = (struct PNGChunkHeader *)((char *)start_chunk + *iter_bytes);

        if (end_ptr <= curr_chunk) {
                *iter_bytes = 0;
                return NULL;
        }

        *iter_bytes += sizeof (struct PNGChunkHeader) + ntohl (curr_chunk->length) + sizeof (uint32_t);

        return curr_chunk;
}

uint8_t *read_all_IDAT_chunk_data (struct PNG *png, size_t png_size, size_t *IDAT_size_buffer)
{
        // first non IHDR chunk starts afer the end of the the PNG struct.
        struct PNGChunkHeader *chunk_header = (struct PNGChunkHeader *)&png->data[0];

        // end of png file, to ensure we don't move off mem mapped region
        void *png_eof = ((char *)png) + png_size;

        // read all the chunks, find the total size of the IDAT chunks
        size_t total_IDAT_size = 0;
        size_t iter_bytes = 0;

        struct PNGChunkHeader *curr_chunk = NULL;

        while ((curr_chunk = iter_chunks (chunk_header, &iter_bytes, png_eof)) != NULL) {
                if (read_chunk_type (curr_chunk->chunk_type) == IDAT_CHUNK_TYPE) {
                        total_IDAT_size += ntohl (curr_chunk->length);
                }
        }

        // copy total IDAT chunk size to user specified buffer
        if (IDAT_size_buffer)
                *IDAT_size_buffer = total_IDAT_size;

        // allocate space for storing IDAT data
        uint8_t *IDAT_data = malloc (total_IDAT_size);

        if (!IDAT_data) {
                perror ("ERROR: malloc");
                exit (EXIT_FAILURE);
        }

        // rewind chunk_header ptr
        chunk_header = (struct PNGChunkHeader *)&png->data[0];

        // copy all IDAT data
        uint8_t *IDAT_data_cursor = IDAT_data;
        while ((curr_chunk = iter_chunks (chunk_header, &iter_bytes, png_eof)) != NULL) {
                if (read_chunk_type (curr_chunk->chunk_type) == IDAT_CHUNK_TYPE) {
                        memcpy (IDAT_data_cursor, curr_chunk->data, ntohl (curr_chunk->length));
                        IDAT_data_cursor += ntohl (curr_chunk->length);
                }
        }

        return IDAT_data;
}

uint8_t *decompress_png (uint8_t *IDAT_data, size_t total_size, size_t *decompressed_size)
{
#define CHUNK (1024 * 5)
        size_t out_buffer_size = total_size * 2;
        uint8_t *IDAT_data_decompressed = malloc (out_buffer_size);

        if (!IDAT_data_decompressed) {
                perror ("ERROR: malloc");
                exit (EXIT_FAILURE);
        }
        z_stream stream = { 0 };
        inflateInit2 ((z_streamp)&stream, 0);
        stream.avail_in = total_size;
        stream.next_in = IDAT_data;
        stream.avail_out = out_buffer_size;
        stream.next_out = IDAT_data_decompressed;
        do {
                int ret = inflate ((z_streamp)&stream, Z_NO_FLUSH);
                switch (ret) {
                case Z_OK: break;
                case Z_STREAM_END: break;
                case Z_NEED_DICT: {
                        ret = Z_DATA_ERROR;
                        break;
                }
                case Z_DATA_ERROR: /* fall through */
                case Z_MEM_ERROR: {
                        (void)inflateEnd ((z_streamp)&stream);
                        return NULL;
                }
                default: {
                        fprintf (stderr, "ERROR: some dumbass shit happened with zlib again.");
                        abort ();
                        break;
                }
                }

                size_t new_buffer_size = out_buffer_size + CHUNK;

                IDAT_data_decompressed = realloc (IDAT_data_decompressed, new_buffer_size);

                if (!IDAT_data_decompressed) {
                        perror ("ERROR: realloc");
                        exit (EXIT_FAILURE);
                }

                stream.next_out = IDAT_data_decompressed + out_buffer_size;
                stream.avail_out += CHUNK;
                out_buffer_size = new_buffer_size;
        } while (stream.total_in != total_size);

        (void)inflateEnd (&stream);

        if (decompressed_size)
                *decompressed_size = out_buffer_size - stream.avail_out;

        return IDAT_data_decompressed;

#undef CHUNK
}

void inverse_filter_none (struct ImageData *data)
{
        return;
}

size_t compute_index (size_t x, size_t y, size_t width, size_t height)
{
        return y * width * 3 + x * 3;
}

uint8_t compute_bpp (struct ImageData *data)
{
        switch (data->color_type) {
        case COLOR_TYPE_GRAYSCALE: return (data->bit_depth * 1 + 7) / 8;
        case COLOR_TYPE_RGB: return (data->bit_depth * 3 + 7) / 8;
        case COLOR_TYPE_GRAYSCALE_ALPHA: return (data->bit_depth * 2 + 7) / 8;
        case COLOR_TYPE_RGBA: return (data->bit_depth * 4 + 7) / 8;
        }

        assert (0 && "ERROR: invalid color type");
}

void inverse_filter_sub (struct ImageData *data)
{
        uint8_t bpp = compute_bpp (data);

        for (size_t y = 0; y < data->height; y++) {
                for (size_t x = 0; x < data->width; x++) {
                        size_t index = compute_index (x, y, data->width, data->height);

                        size_t r_idx = index, g_idx = index + 1, b_idx = index + 2;

                        if (r_idx - bpp >= 0)
                                data->data[r_idx] = data->data[r_idx] + data->data[r_idx - bpp];
                        if (g_idx - bpp >= 0)
                                data->data[g_idx] = data->data[g_idx] + data->data[g_idx - bpp];
                        if (b_idx - bpp >= 0)
                                data->data[b_idx] = data->data[b_idx] + data->data[b_idx - bpp];
                }
        }
}

void inverse_filter_up (struct ImageData *data)
{
        for (size_t y = 1; y < data->height; y++) {
                for (size_t x = 0; x < data->width; x++) {
                        size_t index = compute_index (x, y, data->width, data->height);
                        size_t up = compute_index (x, y - 1, data->width, data->height);
                        data->data[index] += data->data[up];
                        data->data[index + 1] += data->data[up + 1];
                        data->data[index + 2] += data->data[up + 2];
                }
        }
}

void inverse_filter_average (struct ImageData *data)
{
        uint8_t bpp = compute_bpp (data);
}

void read_cmd_args (int argc, char **argv)
{
        int c;
        opterr = 0;
        while ((c = getopt (argc, argv, "f:")) != -1) {
                switch (c) {
                case 'f': png_file_name = optarg; break;
                default: break;
                }
        }
}

int main (int argc, char **argv)
{
        read_cmd_args (argc, argv);

        if (!png_file_name) {
                fprintf (stderr, "ERROR: could not open file, expected PNG file name.");
                return 1;
        }

        int png_fd = open (png_file_name, O_RDWR);

        if (png_fd < 0) {
                perror ("ERROR: open");
                return 1;
        }

        size_t file_size = lseek (png_fd, 0, SEEK_END);

        if (errno) {
                perror ("ERROR: could not get file size: lseek");
                return 1;
        }

        lseek (png_fd, 0, SEEK_SET);

        if (errno) {
                perror ("ERROR: could not rewind file: lseek");
                return 1;
        }

        char *png_file = mmap (NULL, file_size, PROT_READ | PROT_WRITE, MAP_SHARED, png_fd, 0);

        if (!png_file) {
                perror ("ERROR: could not map file to memory: mmap");
                return 1;
        }

        close (png_fd);

        struct PNG *png = (struct PNG *)png_file;

        size_t IDAT_size, decompressed_size;

        struct ImageData img = { .data = decompress_png (read_all_IDAT_chunk_data (png, file_size, &IDAT_size),
                                                         IDAT_size,
                                                         &decompressed_size),
                                 .bit_depth = png->ihdr_chunk.bit_depth,
                                 .color_type = png->ihdr_chunk.color_type,
                                 .width = png->ihdr_chunk.width,
                                 .height = png->ihdr_chunk.height };

        void (*filter) (struct ImageData *) = NULL;

        switch (png->ihdr_chunk.filter_method) {
        case FILTER_NONE: filter = &inverse_filter_none; break;
        case FILTER_SUB: filter = &inverse_filter_sub; break;
        case FILTER_UP: break;
        case FILTER_AVG: break;
        case FILTER_PAETH: break;
        }

        filter (&img);

        printf ("Width: %d, Height: %d", ntohl (png->ihdr_chunk.width), ntohl (png->ihdr_chunk.height));

        return 0;
}
