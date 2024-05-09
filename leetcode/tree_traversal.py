
class Node:

    def __init__(self, left, right, v) -> None:
        self.left = left
        self.right = right
        self.val = v


def in_order_rec(head: 'Node'):
    if head is None:
        return
    in_order_rec(head.left)
    print(head.val)
    in_order_rec(head.right)


def in_order_iter(head: 'Node'):

    st = [(head, False)]

    while len(st) > 0:

        r, left = st.pop()
        if r.left is not None and not left:
            st.append((r, True))
            st.append((r.left, False))
            continue

        print(r.val)

        if r.right is not None:
            st.append((r.right, False))
            continue


in_order_iter(
    Node(
        Node(
            Node(None, None, "A"),
            Node(
                Node(None, None, "C"),
                Node(None, None, "E"),
                "D"),
            "B"),
        Node(
            None,
            Node(
                Node(None, None, "H"),
                None,
                "I"),
            "G"),
        "F")
)
