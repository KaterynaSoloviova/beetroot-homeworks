# Task 1
# Modify the 'depth-first search' to produce strongly connected components

from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, v, visited, stack=None):
        visited[v] = True
        print(v, end=' ')
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, stack)
        stack.append(v)

    def transpose(self):
        graph_transpose = Graph(self.vertices)
        for v in self.graph:
            for neighbor in self.graph[v]:
                graph_transpose.add_edge(neighbor, v)
        return graph_transpose

    def find_scc(self):
        stack = []
        visited = [False] * self.vertices

        for i in range(self.vertices):
            if not visited[i]:
                self.dfs(i, visited, stack)

        g_transpose = self.transpose()

        visited = [False] * self.vertices
        sccs = []

        while stack:
            v = stack.pop()
            if not visited[v]:
                scc_stack = []
                g_transpose.dfs(v, visited, scc_stack)
                sccs.append(scc_stack)

        return sccs


g = Graph(6)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 5)
g.add_edge(4, 3)
g.add_edge(4, 1)
g.add_edge(5, 4)
g.add_edge(5, 0)

sccs = g.find_scc()
print("Strongly Connected Components:")
for scc in sccs:
    print(scc)
