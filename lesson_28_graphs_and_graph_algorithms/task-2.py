# Task 2
# Using breadth-first search write an algorithm that can determine the shortest path from each vertex to every other
# vertex. This is called the all-pairs shortest path problem.

from collections import defaultdict


class Graph:
    def __init__(self):
        self.adj_list = defaultdict(dict)

    def add_edge(self, u, v, weight):
        self.adj_list[u][v] = weight

    def dijkstra(self, start):
        dist = {vertex: float('inf') for vertex in self.adj_list}
        dist[start] = 0
        visited = set()

        queue = [(0, start)]

        while queue:
            queue.sort()
            d, u = queue.pop(0)

            if u in visited:
                continue
            visited.add(u)

            for v, weight in self.adj_list[u].items():
                if v not in visited:
                    new_distance = dist[u] + weight
                    if new_distance < dist[v]:
                        dist[v] = new_distance
                        queue.append((dist[v], v))
        return dist

    def all_pairs_shortest_path(self):
        vertices = list(self.adj_list.keys())
        num_vertices = len(vertices)
        dist = [[float('inf')] * num_vertices for _ in range(num_vertices)]

        for index, vertex in enumerate(vertices):
            dijkstra_result = self.dijkstra(vertex)
            for target_index, target in enumerate(vertices):
                dist[index][target_index] = dijkstra_result[target]

        return dist

    def print_distance_matrix(self, dist):
        print("All-Pairs Shortest Path Distance Matrix:")
        for row in dist:
            print(row)


graph = Graph()
graph.add_edge(0, 1, 1)
graph.add_edge(0, 2, 4)
graph.add_edge(1, 2, 2)
graph.add_edge(1, 3, 5)
graph.add_edge(2, 3, 1)

distance_matrix = graph.all_pairs_shortest_path()
graph.print_distance_matrix(distance_matrix)
