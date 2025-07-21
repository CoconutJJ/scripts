#include <curl/curl.h>
#include <curl/easy.h>
#include <stdlib.h>

int main (int argc, char **argv)
{
        CURL *curl = curl_easy_init ();

        if (!curl)
                exit (EXIT_FAILURE);

        curl_easy_setopt (curl, CURLOPT_URL, "https://license.davidyue.me/?code=ACE");

        CURLcode res = curl_easy_perform (curl);

        if (res != CURLE_OK) {
                fprintf (stderr, "error: unknown\n");
                exit (EXIT_FAILURE);
        }

        long http_code = 0;

        res = curl_easy_getinfo (curl, CURLINFO_RESPONSE_CODE, &http_code);

        if (res != CURLE_OK) {
                fprintf (stderr, "error: unknown\n");
                exit (EXIT_FAILURE);
        }

        if (http_code != 200) {
                fprintf (stderr, "error: unknown\n");
                exit(EXIT_FAILURE);
        }

}
