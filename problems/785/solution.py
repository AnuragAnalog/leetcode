class Solution:
    def check_bipartite(self, node, graph, color):
        q = [node]
        color = [-1] * len(graph)
        color[node] = 0

        while q:
            node = q.pop(0)
            for n in graph[node]:
                if color[n] == -1:
                    color[n] = 1 - color[node]
                    q.append(n)
                elif color[n] == color[node]:
                    return False

        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        V = len(graph)
        color = [-1] * V

        for i in range(V):
            if not self.check_bipartite(i, graph, color):
                return False

        return True
