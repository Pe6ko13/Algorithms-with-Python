def dfs(source, destination, graph, visited):
    if source in visited:
        return

    visited.add(source)

    if source == destination:
        return

    for child in graph[source]:
        dfs(child, destination, graph, visited)



def path_exists(source, destination, graph):
    visited = set()
    dfs(source, destination, graph, visited)
    return destination in visited


nodes = int(input())
graph = {}
edges = []
removed_edges = []

for _ in range(nodes):
    node, children = input().split(' -> ')
    children = children.split()
    graph[node] = children
    for child in children:
        edges.append((node, child))

for source, destination in sorted(edges, key=lambda x: (x[0], x[1])):
    if destination not in graph[source] or source not in graph[destination]:
        continue

    graph[source].remove(destination)
    graph[destination].remove(source)

    if path_exists(source, destination, graph):
        removed_edges.append((source, destination))
    else:
        graph[source].append(destination)
        graph[destination].append(source)

print(f"Edges to remove: {len(removed_edges)}")
for first, second in removed_edges:
    print(f"{first} - {second}")