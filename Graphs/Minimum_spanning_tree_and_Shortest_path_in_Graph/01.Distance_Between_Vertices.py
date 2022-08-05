from collections import deque


def find_shortest_path(graph, source, destination):
    queue = deque([source])
    visited = {source}
    # visited = [False] * len(graph)
    # visited[source] = True

    parent = {source: None}
    # parent = [None] * len(graph)

    while queue:
        node = queue.popleft()
        if node == destination:
            break
        for child in graph[node]:
            # if visited[child]:
            #     continue
            if child in visited:
                continue
            queue.append(child)
            visited.add(child)
            # visited[child] = True
            parent[child] = node

    return parent


nodes = int(input())
pairs = int(input())

graph = {}
# graph = []
# [graph.append([]) for _ in range(nodes + 1)]

for _ in range(nodes):
    node, children_str = input().split(':')
    node = int(node)
    children = [int(x) for x in children_str.split()] if children_str else []
    graph[node] = children

for _ in range(pairs):
    source, destination = [int(x) for x in input().split('-')]

    parent = find_shortest_path(graph, source, destination)

    # if parent[destination] is None:
    if destination not in parent:
        print(f"{{{source}, {destination}}} -> -1")
        continue

    size = 0
    node = destination
    while node is not None:
        node = parent[node]
        size += 1

    print(f"{{{source}, {destination}}} -> {size - 1}")