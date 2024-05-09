#include "helpers.h"
#include <math.h>
#include <stdbool.h>

void grayscale (int height, int width, RGBTRIPLE image[height][width])
{
        for (int i = 0; i < height; i++) {
                for (int j = 0; j < width; j++) {
                        int avg = (image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3;

                        image[i][j].rgbtRed = avg;
                        image[i][j].rgbtBlue = avg;
                        image[i][j].rgbtGreen = avg;
                }
        }
}

// Reflect image horizontally
void reflect (int height, int width, RGBTRIPLE image[height][width])
{
        for (int i = 0; i < height; i++) {
                for (int j = 0; j < width; j++) {
                        RGBTRIPLE *fst = &(image[i][j]);
                        RGBTRIPLE *snd = &(image[i][width - j - 1]);
                        RGBTRIPLE tmp = *fst;
                        *fst = *snd;
                        *snd = tmp;
                }
        }
}

bool get_neighbours (int x, int y, int height, int width, int *new_x, int *new_y, int *count)
{
        int neighbours[9][2] = {
                {-1, -1},
                { 0, -1},
                { 1, -1},
                {-1,  0},
                { 0,  0},
                { 1,  0},
                {-1,  1},
                { 0,  1},
                { 1,  1}
        };

        for (int i = *count; i < 9; i++) {
                int x_tmp = x + neighbours[i][0], y_tmp = y + neighbours[i][1];

                if (x_tmp < 0 || x_tmp >= width)
                        continue;

                if (y_tmp < 0 || y_tmp >= height)
                        continue;

                *new_x = x_tmp;
                *new_y = y_tmp;
                *count = i + 1;

                return true;
        }

        return false;
}

// Blur image
void blur (int height, int width, RGBTRIPLE image[height][width])
{
        for (int x = 0; x < width; x++) {
                for (int y = 0; y < height; y++) {
                        int nx, ny, count = 0, r_sum = 0, g_sum = 0, b_sum = 0;
                        int neighbour_count = 0;
                        while (get_neighbours (x, y, height, width, &nx, &ny, &count)) {
                                r_sum += image[ny][nx].rgbtRed;
                                b_sum += image[ny][nx].rgbtBlue;
                                g_sum += image[ny][nx].rgbtGreen;

                                neighbour_count++;
                        }

                        image[y][x].rgbtBlue = b_sum / neighbour_count;
                        image[y][x].rgbtGreen = g_sum / neighbour_count;
                        image[y][x].rgbtRed = r_sum / neighbour_count;
                }
        }

        return;
}

int isqrt (int n)
{
        double v = (double)n;

        return (int)lround (sqrt (v));
}

// Detect edges
void edges (int height, int width, RGBTRIPLE image[height][width])
{
        int Gx[3][3] = {
                {-1, 0, 1},
                {-2, 0, 2},
                {-1, 0, 1}
        };

        int Gy[3][3] = {
                {-1, -2, -1},
                { 0,  0,  0},
                { 1,  2,  1}
        };

        RGBTRIPLE new_image[height][width];

        for (int x = 0; x < width; x++) {
                for (int y = 0; y < height; y++) {
                        int new_x, new_y, count = 0, xr_sum = 0, yr_sum = 0, xg_sum = 0, yg_sum = 0, xb_sum = 0,
                                          yb_sum = 0;

                        while (get_neighbours (x, y, height, width, &new_x, &new_y, &count)) {
                                int dx = 1 + new_x - x, dy = 1 + new_y - y;

                                xr_sum += image[new_y][new_x].rgbtRed * Gx[dy][dx];
                                xb_sum += image[new_y][new_x].rgbtBlue * Gx[dy][dx];
                                xg_sum += image[new_y][new_x].rgbtGreen * Gx[dy][dx];

                                yr_sum += image[new_y][new_x].rgbtRed * Gy[dy][dx];
                                yb_sum += image[new_y][new_x].rgbtBlue * Gy[dy][dx];
                                yg_sum += image[new_y][new_x].rgbtGreen * Gy[dy][dx];
                        }

                        new_image[y][x].rgbtRed = isqrt (xr_sum * xr_sum + yr_sum * yr_sum);
                        new_image[y][x].rgbtBlue = isqrt (xb_sum * xb_sum + yb_sum * yb_sum);
                        new_image[y][x].rgbtGreen = isqrt (xg_sum * xg_sum + yg_sum * yg_sum);
                }
        }
        for (int x = 0; x < width; x++) {
                for (int y = 0; y < height; y++) {
                        image[y][x] = new_image[y][x];
                }
        }

        return;
}
