from queue import PriorityQueue


class Edge:
    def __init__(self, first, second, distance):
        self.first = first
        self.second = second
        self.distance = distance

    def __gt__(self, other):
        return self.distance > other.distance


def cala_damage(jumps, damage):
    for _ in range(jumps):
        damage //= 2
    return damage


def prim(node, damage, damage_by_node, graph):
    damage_by_node[node] += damage
    tree = {node}
    jumps = [0] * len(graph)

    pq = PriorityQueue()
    [pq.put(edge) for edge in graph[node]]

    while not pq.empty():
        min_edge = pq.get()

        tree_node, non_tree_node = -1, -1

        if min_edge.first in tree and min_edge.second not in tree:
            tree_node, non_tree_node = min_edge.first, min_edge.second
        if min_edge.first not in tree and min_edge.second in tree:
            non_tree_node, tree_node = min_edge.first, min_edge.second
        if non_tree_node == -1:
            continue

        jumps[non_tree_node] = jumps[tree_node] + 1
        damage_by_node[non_tree_node] += cala_damage(jumps[non_tree_node], damage)
        tree.add(non_tree_node)
        [pq.put(edge) for edge in graph[non_tree_node]]


nodes = int(input())
edges = int(input())
lightnings = int(input())

graph = {node: [] for node in range(nodes)}

for _ in range(edges):
    first, second, distance = [int(x) for x in input().split()]
    edge = Edge(first, second, distance)
    graph[first].append(edge)
    graph[second].append(edge)

damage_by_node = [0] * nodes

for _ in range(lightnings):
    node, damage = [int(x) for x in input().split()]
    prim(node, damage, damage_by_node, graph)

print((damage_by_node))