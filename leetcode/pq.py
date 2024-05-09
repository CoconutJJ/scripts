
from typing import Callable


class PriorityQueue:

    def __init__(self, key: Callable[[any], str | int]) -> None:
        self.q = []
        self.key = key
        self.indexes = dict()

    def __len__(self):
        return len(self.q)

    def _parent(i):
        return (i - 1) // 2

    def _lchild(i):
        return 2 * i + 1

    def _rchild(i):
        return 2 * i + 2

    def _percdown(self, i):

        while self._lchild(i) < len(self.q):
            curr_pri, curr = self.q[i]

            l_pri, l = self.q[self._lchild(i)]

            r_pri, r = None, None

            if self._rchild(i) >= len(self.q):
                r_pri = float('inf')
            else:
                r_pri, r = self.q[self._rchild(i)]

            if curr_pri < min(l_pri, r_pri):
                break

            if l_pri < r_pri:

                self.q[self._lchild(i)] = (curr_pri, curr)
                self.q[i] = (l_pri, l)

                self.indexes[self.key(curr)] = self._lchild(i)
                self.indexes[self.key(l)] = i
                i = self._lchild(i)

            else:
                self.q[self._rchild(i)] = (curr_pri, curr)
                self.q[i] = (r_pri, r)

                self.indexes[self.key(curr)] = self._rchild(i)
                self.indexes[self.key(r)] = i
                i = self._rchild(i)

    def _percup(self, i):

        while self._parent(i) >= 0:

            parent_pri, p = self.q[self._parent(i)]

            curr_pri, curr = self.q[i]

            if curr_pri >= parent_pri:
                break

            self.q[i] = (parent_pri, p)
            self.q[self._parent(i)] = (curr_pri, curr)

            self.indexes[self.key(curr)] = self._parent(i)
            self.indexes[self.key(p)] = i
            i = self._parent(i)

    def insert(self, elem, pri):

        self.q.append((pri, elem))

        self._percup(len(self.q) - 1)

    def pop(self):

        pri, item = self.q.pop(0)

        last = self.q[-1]

        self.q = [last] + self.q[:-1]

        self._percdown(0)

        del self.indexes[self.key(item)]

        return (pri, item)
