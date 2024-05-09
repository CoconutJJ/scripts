#include "cs50.h"
#include <limits.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX 10

typedef struct vote_pair {
        int winner;
        int loser;
} vote_pair;

int num_candidates = 0;
int preference_matrix[MAX][MAX] = { 0 }, adjacency_matrix[MAX][MAX] = { 0 };
vote_pair pairs[MAX * (MAX - 1) / 2] = { 0 };

int get_candidate_id (char *candidate, char **candidates)
{
        for (int i = 0; candidates[i] != NULL; i++) {
                if (strcmp (candidate, candidates[i]) == 0)
                        return i;
        }

        return -1;
}

void cast_vote (char **candidates)
{
        int ranking[MAX];
        for (int i = 0; i < num_candidates; i++) {
                int candidate_id;
                char *candidate_name;
                while (1) {
                        printf ("Rank %d: ", i + 1);

                        candidate_name = get_string ("");

                        candidate_id = get_candidate_id (candidate_name, candidates);

                        if (candidate_id != -1)
                                break;

                        printf ("Invalid candidate name. Try again.\n");
                        free (candidate_name);
                }
                ranking[i] = candidate_id;
        }

        for (int i = 0; i < num_candidates - 1; i++)
                for (int j = i + 1; j < num_candidates; j++)
                        preference_matrix[ranking[i]][ranking[j]]++;
}

void sort_pairs (vote_pair *pairs, int size)
{
        for (int i = 0; i < size - 1; i++) {
                for (int j = i + 1; j < size; j++) {
                        int fst = preference_matrix[pairs[i].winner][pairs[i].loser];
                        int snd = preference_matrix[pairs[j].winner][pairs[j].loser];

                        if (fst > snd) {
                                vote_pair tmp = pairs[i];
                                pairs[i] = pairs[j];
                                pairs[j] = tmp;
                        }
                }
        }
}

void add_pair (vote_pair pair)
{
        adjacency_matrix[pair.winner][pair.loser] = 1;
}

void remove_pair (vote_pair pair)
{
        adjacency_matrix[pair.winner][pair.loser] = 0;
}

bool has_cycle (int start_candidate)
{
        int stack[MAX * (MAX - 1) / 2], stack_top = 1;
        size_t visited_stack[MAX * (MAX - 1) / 2];

        stack[0] = start_candidate;
        visited_stack[0] = 0;

        while (stack_top != 0) {
                stack_top--;
                int candidate = stack[stack_top];
                size_t visited = visited_stack[stack_top];

                if (visited & (1 << candidate))
                        return true;

                visited |= (1 << candidate);

                for (int i = 0; i < num_candidates; i++) {
                        if (adjacency_matrix[candidate][i]) {
                                stack[stack_top] = i;
                                visited_stack[stack_top] = visited;
                                stack_top++;
                        }
                }
        }

        return false;
}

int compute_pairs ()
{
        int count = 0;

        for (int i = 0; i < num_candidates - 1; i++) {
                for (int j = i + 1; j < num_candidates; j++) {
                        if (preference_matrix[i][j] > preference_matrix[j][i]) {
                                pairs[count].winner = i;
                                pairs[count].loser = j;
                        } else {
                                pairs[count].winner = j;
                                pairs[count].loser = i;
                        }
                        count++;
                }
        }

        sort_pairs (pairs, count);

        return count;
}

void compute_graph (int count)
{
        int curr = count - 1;

        while (curr >= 0) {
                add_pair (pairs[curr]);

                if (has_cycle (pairs[curr].winner))
                        remove_pair (pairs[curr]);
                curr--;
        }
}

int find_winner ()
{
        for (int c = 0; c < num_candidates; c++) {
                bool is_winner = true;
                for (int s = 0; s < num_candidates; s++) {
                        if (adjacency_matrix[s][c])
                                is_winner = false;
                }

                if (is_winner)
                        return c;
        }

        return -1;
}

int main (int argc, char **argv)
{
        if (argc - 1 < 2) {
                fprintf (stderr, "Must have at least 2 candidates.");
                exit (EXIT_FAILURE);
        }

        if (argc - 1 > MAX) {
                fprintf (stderr, "Sorry, only %d candidates maximum.", MAX);
                exit (EXIT_FAILURE);
        }

        num_candidates = argc - 1;

        int num_voters = get_int ("Number of voters: ");

        for (int i = 0; i < num_voters; i++) {
                cast_vote (&(argv[1]));
        }

        compute_graph (compute_pairs ());

        int winner_candidate = find_winner ();

        printf ("%s\n", argv[winner_candidate + 1]);
}