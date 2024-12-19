
type Graph = dict[int, list[int]]

def dfs(node: int, graph: Graph, visited: set):

    nodes = []
    visited.add(node)

    for child in graph[node]:

        if child in visited:
            continue


        nodes.extend(dfs(child, graph, visited))
    
    nodes.append(node)

    return nodes

def graph_transpose(graph: Graph):

    transpose = dict()


    for key in graph:
        for child in graph[key]:

            transpose[child] = transpose.get(child, []) + [key]

    return transpose

def kosaraju(root: int, graph: Graph):

    dfs_order = dfs(root, graph, set())
    nodes = set()
    sccs = []
    graph_t = graph_transpose(graph)

    for rep in reversed(dfs_order):

        if rep in nodes:
            continue

        scc = dfs(rep, graph_t, nodes)
        sccs.append(scc)
        nodes.update(scc)

    return sccs


if __name__ == "__main__":

    graph = {
        1: [2],
        2: [3,4,5],
        3: [1,4],
        4: [],
        5: [6,7],
        6: [8],
        7: [6],
        8: [7]

    }

    print(kosaraju(1, graph))


    pass



