
class Node:

    def __init__(self) -> None:
        self.left = None
        self.right = None
        self.value = None
        self.closest_pair = None


def insert(tree: 'Node', ins: 'Node'):

    if tree is None:
        return ins

    if ins.value < tree.value:
        tree.left = insert(tree.left, ins)
    else:
        tree.right = insert(tree.right, ins)

    def closest(r): return abs(r[0] - r[1]) if r is not None else float('inf')

    tree.closest_pair = min(
        tree.closest_pair,
        tree.left.closest_pair,
        tree.right.closest_pair,
        [tree.value, ins.value],
        key=closest)

    return tree


def find_delete_replacement(node: 'Node'):

    if node.left is None:
        return node.right

    node = node.left

    if node.right is None:
        return node

    parent = None
    while node.right is not None:
        parent = node
        node = node.right

    parent.right = node.left

    return node


def delete(tree: 'Node', value: int):

    if tree.value == value:

        new_node = find_delete_replacement(tree)

        if new_node is None:
            return None

        new_node.left = tree.left
        new_node.right = tree.right

        return new_node

    if value < tree.value:

        tree.left = delete(tree.left, value)

    else:

        tree.right = delete(tree.right, value)
