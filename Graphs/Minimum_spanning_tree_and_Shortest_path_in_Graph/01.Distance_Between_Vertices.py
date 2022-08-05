from collections import deque


def find_shortest_path(graph, source, destination):
    queue = deque([source])
    visited = {source}

    parent = {source: None}

    while queue:
        node = queue.popleft()
        if node == destination:
            break
        for child in graph[node]:
            if child in visited:
                continue
            queue.append(child)
            visited.add(child)
            parent[child] = node

    return parent


nodes = int(input())
pairs = int(input())

graph = {}

for _ in range(nodes):
    node, children_str = input().split(':')
    node = int(node)
    children = [int(x) for x in children_str.split()] if children_str else []
    graph[node] = children

for _ in range(pairs):
    source, destination = [int(x) for x in input().split('-')]

    parent = find_shortest_path(graph, source, destination)

    if destination not in parent:
        print(f"{{{source}, {destination}}} -> -1")
        continue

    size = 0
    node = destination
    while node is not None:
        node = parent[node]
        size += 1

    print(f"{{{source}, {destination}}} -> {size - 1}")