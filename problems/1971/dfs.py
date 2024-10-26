class Solution:
    def dfs(self, node, adj, visited, dest):
        visited[node] = 1
        if node == dest:
            return True

        for n in adj[node]:
            if visited[n] == 0:
                if self.dfs(n, adj, visited, dest):
                    return True

        return False

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = [[] for _ in range(n)]
        visited = [0] * n

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        return self.dfs(source, adj, visited, destination)
