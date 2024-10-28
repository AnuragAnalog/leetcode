class Solution:
    def dfs(self, node, dst, adj, visited):
        visited[node] = 1
        if node == dst:
            return True

        for n in adj[node]:
            if visited[n] == 0:
                if self.dfs(n, dst, adj, visited):
                    return True

    def reach(self, src, dst, adj):
        visited = [0] * len(adj)

        return self.dfs(src, dst, adj, visited)

    def equationsPossible(self, equations: List[str]) -> bool:
        adj = [[] for _ in range(26)]

        for equation in equations:
            if equation[1:3] == "!=":
                continue

            u = ord(equation[0]) - 97
            v = ord(equation[-1]) - 97
            adj[u].append(v)
            adj[v].append(u)

        for equation in equations:
            if equation[1:3] == "==":
                continue

            u = ord(equation[0]) - 97
            v = ord(equation[-1]) - 97
            if self.reach(u, v, adj):
                return False

        return True
