# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def distributeCoins(root):

    parent_of = dict()

    q = [root]
    parent_of[id(root)] = None
    starts = []

    while len(q) != 0:

        curr = q.pop(0)

        if curr.val > 1:

            starts.append(curr)

        if curr.left is not None:
            q.append(curr.left)
            parent_of[id(curr.left)] = curr

        if curr.right is not None:
            q.append(curr.right)
            parent_of[id(curr.right)] = curr

    steps = 0
    visited = set()

    for s in starts:

        coins_available = s.val - 1
        dist_to_parent = dict()

        s.val = 1
        q = [s]

        dist_to_parent[id(s)] = 0

        while len(q) != 0:

            if coins_available == 0:
                break

            curr = q.pop(0)
            visited.add(id(curr))
            if curr.val == 0:

                curr.val = 1
                steps += dist_to_parent[id(curr)]
                coins_available -= 1

            neighbours = [curr.left, curr.right, parent_of[id(curr)]]

            for n in neighbours:

                if n is None or id(n) in visited:
                    continue

                dist_to_parent[id(n)] = dist_to_parent[id(curr)] + 1
                q.append(n)

    return steps


r = TreeNode(1)

r.left = TreeNode(3)
r.right = TreeNode(0)

print(distributeCoins(r))
