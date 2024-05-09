"""
Python Priority Queue

pop() - O(log n)
push() - O(log n)
changePriority - O(log n)

Author: David Yue <davidyue5819@gmail.com>
"""


class PriorityQueue:

    def __init__(self):

        super().__init__()

        self.q = [()]
        self.index = dict()

    def __len__(self):

        return len(self.q) - 1

    def __perc_up(self, idx):
        """
            Percolate the object at index `idx` up the heap
        """
        r, p = self.q[idx]

        curr_idx = idx

        while (cmp_idx := self.__parent_idx(curr_idx)) != 0:

            cmp_r, cmp_p = self.q[cmp_idx]

            if cmp_p > p:

                self.q[cmp_idx], self.q[curr_idx] = self.q[curr_idx], self.q[cmp_idx]

                self.index[id(cmp_r)], self.index[id(
                    r)] = self.index[id(r)], self.index[id(cmp_r)]

                curr_idx = cmp_idx
            else:
                break

    def __perc_down(self, idx):
        """
            Percolate the object at index `idx` down the heap
        """

        r, p = self.q[idx]

        curr_idx = idx

        while (
            cmp_idx := min(
                self.__left_child_idx(curr_idx),
                self.__right_child_idx(curr_idx),
                key=lambda j: self.q[j][1] if j < len(
                    self.q) else float('inf'))) < len(
                self.q):

            cmp_r, cmp_p = self.q[cmp_idx]

            if cmp_p < p:
                self.q[cmp_idx], self.q[curr_idx] = self.q[curr_idx], self.q[cmp_idx]
                self.index[id(cmp_r)], self.index[id(
                    r)] = self.index[id(r)], self.index[id(cmp_r)]
                curr_idx = cmp_idx
            else:
                break

    def pop(self):
        """
            Pops the first item on the Priority Queue
            >>> pq = PriorityQueue()
            >>> pq.push(1,2)
            >>> pq.pop()
            1
        """
        if len(self.q) == 1:
            return None

        obj, p = self.q.pop(1)

        del self.index[id(obj)]

        if len(self.q) != 1:

            last_obj, last_p = self.q.pop()

            self.index[id(last_obj)] = 1

            self.q.insert(1, (last_obj, last_p))

            self.__perc_down(1)

        return obj

    def push(self, obj: object, priority: int):
        """
            Pushes a new `obj` into the priority queue with priority
            `priority`
        """
        self.q.append((obj, priority))

        self.index[id(obj)] = len(self.q) - 1

        self.__perc_up(len(self.q) - 1)

    def peek(self):

        if len(self.q) == 1:
            return None

        obj, _ = self.q[1]

        return obj

    def changePriority(self, obj: object, priority: int) -> bool:
        """
            Change the priority of the object `obj` in the priority queue.
            Returns False if `obj` does not exist in queue. True otherwise.
        """

        if obj not in self:
            return False

        i = self.index[id(obj)]

        r, p = self.q[i]

        self.q[i] = (r, priority)

        if priority < p:
            self.__perc_up(i)
        else:
            self.__perc_down(i)

        return True

    def __str__(self):

        sorted_q = sorted(self.q[1:], key=lambda r: r[1])

        return str(list(map(lambda r: r[0], sorted_q)))

    def __contains__(self, r: object):
        return id(r) in self.index

    def __parent_idx(self, idx):
        return idx // 2

    def __left_child_idx(self, idx):
        return 2 * idx

    def __right_child_idx(self, idx):
        return 2 * idx + 1


if __name__ == "__main__":

    import doctest

    doctest.testmod()
