def find_dependencies(graph):
    result = {}
    for node, children in graph.items():
        if node not in result:
            result[node] = 0
        for child in children:
            if child not in result:
                result[child] = 1
            else:
                result[child] += 1
    return result


def find_node_without_dependencies(dependencies_by_node):
    for node, depend in dependencies_by_node.items():
        if depend == 0:
            return node
    return None


nodes = int(input())

graph = {}
has_cycles = False
sorted_nodes = []

for _ in range(nodes):
    line_parts = input().split('->')
    node = line_parts[0].strip()
    children = line_parts[1].strip().split(', ') if line_parts[1] else []
    graph[node] = children

dependencies_by_node = find_dependencies(graph)

while dependencies_by_node:
    node_to_remove = find_node_without_dependencies(dependencies_by_node)
    if node_to_remove is None:
        has_cycles = True
        break

    dependencies_by_node.pop(node_to_remove)
    sorted_nodes.append(node_to_remove)
    for child in graph(node_to_remove):
        dependencies_by_node[child] -= 1

if has_cycles:
    print('Invalid topological sorting')
else:
    print(f"Topological sorting: {'. '.join(sorted_nodes)}")



# Second solution:
#
# from collections import deque
#
# nodes = int(input())
#
# for _ in range(nodes):
#     line_parts = input().split('->')
#     node = line_parts[0].strip()
#     children = line_parts[1].strip().split(', ') if line_parts[1] else []
#     graph[node] = children
#
#
# visited = set()
# cycles = set()
#
# def dfs(node, graph, visited, cycles, sorted_nodes):
#     if node in cycles:
#         raise Exception
#     if node in visited:
#         return
#     visited.add(node)
#     cycles.add(node)
#
#     for child in graph[node]:
#         dfs(child, graph, visited, cycles, sorted_nodes)
#
#     cycles.remove(node)
#     sorted_nodes.appendleft(node)
#
# sorted_nodes = deque()
#
# for node in graph:
#     dfs(node, graph, visited, cycles, sorted_nodes)
#
# print(*sorted_nodes, sep=' ')