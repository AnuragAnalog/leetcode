class Solution:
    def two_colors(self, n, adj, visited):
        q = [n]
        visited[n] = 0
        
        while q:
            node = q.pop()
            for n in adj[node]:
                if visited[n] == -1:
                    visited[n] = 1 - visited[node]
                    q.append(n)
                elif visited[n] == visited[node]:
                    return False
    
        return True

	def isBipartite(self, V, adj):
	   visited = [-1] * V
	    
	   for v in range(V):
	       if visited[v] == -1:
	           if not self.two_colors(v, adj, visited):
	               return False
	   return True
