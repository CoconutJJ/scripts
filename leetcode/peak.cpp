
#include <cstddef>
#include <vector>
struct Node {
        int value;
        struct Node *next;
};

/**
        The following program is supposed to find the last node in a linked
        list. But it contains a bug.

        First describe what the bug is and fix the bug.

*/

struct Node *findLastNode (struct Node *head)
{
        while (head != nullptr) 
                head = head->next;
        

        return head;
}

/**
        The following binary search algorithm contains a bug.
        Fix the bug.

        Assume L is always sorted.   
*/

bool listContains(std::vector<int> L, int elem) {

        size_t l = 0, r = L.size() - 1;

        while (l < r) {

                size_t m = (l + r) / 2; // assume this will never overflow

                if (L[m] < elem) {
                        l = m;
                } else {
                        r = m;
                }
        }

        return L[l] == elem;
}




int main (int argc, char **argv)
{
}
