
def find_path(G: dict[str, list[str]],
              W: dict[tuple[str, str], int], s: str, t: str):

    st = [(s, float('inf'), [s])]

    visited = set()

    while len(st) != 0:

        r, flow, path = st.pop()

        visited.add(r)
        if r == t:
            return (path, flow)

        for neighbour in G[r]:
            path = path + [neighbour]

            if W[(r, neighbour)] != 0 and neighbour not in visited:
                st.append((neighbour, min(flow, W[r, neighbour]), path))

    return None


def ford_fulkerson(G: dict[str, list[str]],
                   W: dict[tuple[str, str], int], s: str, t: str):

    while (res := find_path(G, W, s, t)) is not None:

        path, flow = res

        for u, v in zip(path[:-1], path[1:]):
            W[(u, v)] -= flow
            W[(v, u)] += flow
