def numBusesToDestination(routes: list[list[int]], source: int, target: int) -> int:
    graph = dict()

    for bus_no, route in enumerate(routes):
        for s, t in zip(route[:-1], route[1:]):
            if s not in graph:
                graph[s] = []

            graph[s].append((bus_no, t))

        first = route[0]
        last = route[-1]

        if last not in graph:
            graph[last] = []

        graph[last].append((bus_no, first))

    q = [(source, 0, -1)]
    visited = set([source])
    while len(q) != 0:
        r, p, bus_no = q.pop(0)

        if r == target:
            return p

        for nb, n  in graph[r]:
            if n in visited:
                continue

            visited.add(n)

            if nb != bus_no:
                q.append((n, p + 1, nb))
            else:
                q.append((n, p, nb))

    return -1


routes = [[1, 2, 7], [3, 6, 7]]

print(numBusesToDestination(routes, 1, 6))
