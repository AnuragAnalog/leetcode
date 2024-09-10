class Solution:
    def __init__(self):
        self.topo_q = list()
        self.topo_sort = list()
        
    def insert_zero_indeg(self, V, in_degree):
        for i in range(V):
            if in_degree[i] == 0:
                self.topo_q.append(i)
                in_degree[i] = -1

    def topoSort(self, V, adj):
        in_degree = [0] * V
        for i in range(V):
            for n in adj[i]:
                in_degree[n] += 1

        self.insert_zero_indeg(V, in_degree)
                
        while self.topo_q:
            node = self.topo_q.pop(0)
            for n in adj[node]:
                in_degree[n] -= 1
                if in_degree[n] == 0:
                    self.topo_q.append(n)
                    in_degree[n] = -1
            self.topo_sort.append(node)

        return self.topo_sort
