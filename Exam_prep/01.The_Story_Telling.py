from collections import deque


def dfs(n, graph, visited, result):
    if n in visited:
        return

    visited.add(n)

    for child in graph[n]:
        dfs(child, graph, visited, result)

    result.appendleft(n)
    print(result)


graph = {}

while True:
    line = input()
    if line == 'End':
        break
    node, children_str = [x.strip() for x in line.split('->')]
    children = children_str.split()
    graph[node] = children

visited = set()
result = deque()

for n in graph:
    dfs(n, graph, visited, result)

print(' '.join(result))