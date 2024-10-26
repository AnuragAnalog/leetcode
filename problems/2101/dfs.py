class Solution:
    def within_radius(self, p1, p2, r):
        if (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 <= r**2:
            return True
        return False

    def dfs(self, node, adj, visited, count):
        visited[node] = 1

        for n in adj[node]:
            if visited[n] == 0:
                count = self.dfs(n, adj, visited, count + 1)

        return count

    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        V = len(bombs)
        adj = [[] for _ in range(V)]

        for i, bomb in enumerate(bombs):
            for j in range(V):
                if i == j:
                    continue
                if self.within_radius(bomb, bombs[j], bomb[2]):
                    adj[i].append(j)

        maxi = 0
        for i in range(V):
            visited = [0] * V
            maxi = max(maxi, self.dfs(i, adj, visited, 1))

        return maxi
