from typing import List

class Solution:
    def check(self, src, adj):
		visited = [0] * V
		stack = [(src, -1)]
		
		while stack:
		    node = stack.pop()
		    visited[node[0]] = 1
		    for n in adj[node[0]]:
		        if node[1] == n:
		            continue
		        if visited[n] == 1:
		            return True
		        visited[node[0]] = 1
		        stack.append((n, node[0]))
		        
	    return False

	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		for i in range(V):
		    if self.check(i, adj):
		        return True
		        
		return False
