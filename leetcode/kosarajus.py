# Kosaraju's Algorithm finds all strongly connected components in a graph

def dfs(root: str, adj: dict[str, list[str]], visited: set):
    visit_stack = []
    tr = dict()

    def rec(start: str):
        visited.add(start)

        for n in adj[start]:

            # compute the transpose graph while doing DFS
            if n not in tr:
                tr[n] = []

            tr[n].append(start)

            if n in visited:
                continue

            visited.add(n)
            rec(n)

        # push each node to stack after all it's neighbours have been visited
        # we use a stack because we would like to find a SCC sink node (i.e a
        # node within a SCC that can only reach nodes within that SCC)
        visit_stack.append(start)

    rec(root)

    return visit_stack, tr


def kosaraju(root: str, adj: dict[str, list[str]]):

    st, transpose = dfs(root, adj, set())
    sccs = []
    visited = set()

    while len(st) != 0:

        r = st.pop()

        if r in visited:
            continue

        # pass in all the visited components so far
        component, _ = dfs(r, transpose, visited)
        visited = visited.union(component)
        sccs.append(component)

    return sccs


print(kosaraju('a', {
    "a": ["b"],
    "b": ["c"],
    "c": ["a", "d"],
    "d": ["e"],
    "e": ["f"],
    "f": ["g"],
    "g": ["d"]
}))


# In a city that has only one-way roads connecting major
# neighborhoods find the smallest number of warehouses that
# Amazon needs to build so that all neighborhoods can be
# served by delivery vans. Each van starts and ends the day
# in its home warehouse.

def dfs(root: str, adj: dict[str, list[str]], visited: set):

    visit_st = []
    transpose_adj = dict()

    def rec(r: str):
        visited.add(r)

        for n in adj[r]:

            if n not in transpose_adj:
                transpose_adj[n] = []

            transpose_adj[n].append(start)

            if n in visited:
                continue

            rec(n)

        visit_st.append(n)

    rec(root)

    return visit_st, transpose_adj


def minWarehouses(G: dict[str, list[str]]):

    visit_stack = []
    visited = set()

    transpose = dict()

    for k in G:  # O(|V|)

        if k not in visited:
            st, tr = dfs(k, G, visited)

            for k in tr:  # O(|V|)
                transpose[k] = tr[k]

            visit_stack += st
            visited = visited.union(st)

    visited = set()

    groups = []

    while len(visit_stack) != 0:

        r = visit_stack.pop()

        if r in visited:
            continue

        scc, _ = dfs(r, transpose, visited)
        visited = visited.union(scc)
        groups.append(scc)

    return len(groups)
