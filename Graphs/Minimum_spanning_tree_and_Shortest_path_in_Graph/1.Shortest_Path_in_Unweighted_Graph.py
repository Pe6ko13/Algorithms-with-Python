from collections import deque


def find_parent_by_node(graph, start, end):
    visited = [False] * len(graph)
    parent = [None] * len(graph)

    visited[start] = True
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node == end:
            break
        for child in graph[node]:
            if visited[child]:
                continue
            visited[child] = True
            queue.append(child)
            parent[child] = node

    return parent


nodes = int(input())
edges = int(input())

graph = []
[graph.append([]) for _ in range(nodes + 1)]

for _ in range(edges):
    source, destination = [int(x) for x in input().split()]
    graph[source].append(destination)

start = int(input())
end = int(input())

parent = find_parent_by_node(graph, start, end)

path = []
node = end
while node is not None:
    path.append(node)
    node = parent[node]

print(f"Shortest path length is: {len(path)}")
print(*list(reversed(path)), sep=' ')
