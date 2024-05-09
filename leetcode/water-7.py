from collections import defaultdict
import heapq


def countEdges(root, edgeDict):

    q = [root]

    edges = 0

    visited = set()

    while len(q) != 0:

        r = q.pop()
        visited.add(r)
        for v in edgeDict[r]:

            if v not in visited:
                q.append(v)
                edges += 1

    return (edges, visited)


def water7(nodes, edges, supply):

    nodes_set = set([i for i in range(1, nodes + 1)])

    edge_dict = defaultdict(set)

    total_edges = 0

    max_supply_component_count = 0

    for u, v in edges:
        edge_dict[u].add(v)
        edge_dict[v].add(u)

    for c in supply:

        edgeCount, componentNodes = countEdges(c, edge_dict)
        nodes_set = nodes_set - componentNodes
        max_supply_component_count = max(
            len(componentNodes), max_supply_component_count)
        N = len(componentNodes)
        total_edges += (N * (N - 1) / 2 - edgeCount)

    unconn_component = []

    while len(nodes_set) != 0:

        r = nodes_set.pop()
        e, s = countEdges(r, edge_dict)
        N = len(s)
        s.remove(r)
        nodes_set = nodes_set - s
        total_edges += (N * (N - 1) / 2 - e)
        heapq.heappush(unconn_component, N)

    curr_cost = 0
    size = heapq.heappop(unconn_component)

    while len(unconn_component) != 0:

        r = heapq.heappop(unconn_component)
        curr_cost += size * r
        total_edges += size * r
        size += r

    print(total_edges, size * max_supply_component_count)
    curr_cost += (size * max_supply_component_count)
    total_edges += (size * max_supply_component_count)

    return (total_edges, curr_cost)


print(water7(12, [(1, 2), (1, 3), (4, 5), (4, 6),
                  (5, 7), (9, 10), (11, 12)], [1, 4]))
