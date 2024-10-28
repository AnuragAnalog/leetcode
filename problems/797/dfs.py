class Solution:
    def __init__(self):
        self.res = list()

    def dfs(self, node, adj, path):
        if node == self.final:
            self.res.append(path)

        for n in adj[node]:
            self.dfs(n, adj, path + [n])

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.start = 0
        self.final = len(graph) - 1

        self.dfs(0, graph, [0])

        return self.res
