import random
from typing import Callable


class Point:
    def __init__(self, xy) -> None:
        self.pt = xy
        self.left = None
        self.right = None


def kthSmallest(L: list[Point], k: int, key: Callable):

    l = []
    r = []

    pt = random.choice(L)

    for p in L:

        if key(p) < key(pt):
            l.append(p)
        else:
            r.append(p)

    if len(l) == k:
        return pt
    elif len(l) < k:
        return kthSmallest(r, k - len(l), key)
    else:
        return kthSmallest(l, k, key)


def buildKdTree(L: list[Point]):

    def build(points: list[Point], split_key: int):

        if len(points) == 0:
            return None

        pt = kthSmallest(points, len(points) // 2, lambda p: p.pt[split_key])

        l = []
        r = []

        for p in points:

            if p is pt:
                continue

            if p.pt[split_key] < pt.pt[split_key]:
                l.append(p)
            else:
                r.append(p)

        pt.left = build(l, 1 - split_key)
        pt.right = build(r, 1 - split_key)

        return pt

    return build(L, 0)


def closestPoint(tree: Point, pt: Point):

    pass
