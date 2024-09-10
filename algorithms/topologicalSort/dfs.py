class Solution:
    def __init__(self):
        self.topo_sort = list()

    def dfs(self, node, visited, adj):
        for n in adj[node]:
            if not visited[n]:
                visited[n] = 1
                self.dfs(n, visited, adj)
                self.topo_sort.append(n)
            
    def topoSort(self, V, adj):
        visited = [0] * V
        for i in range(V):
            if not visited[i]:
                visited[i] = 1
                self.dfs(i, visited, adj)
                self.topo_sort.append(i)

        return self.topo_sort[::-1]
