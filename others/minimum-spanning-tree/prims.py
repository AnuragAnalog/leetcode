import heapq
from typing import List
    
class Solution:
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V: int, adj: List[List[int]]) -> int:
        mst = 0
        visited = [0] * V
        q = list()
        heapq.heappush(q, (0, 0, -1))
        
        while q:
            wt, node, parent = heapq.heappop(q)
            if visited[node] == 0:
                mst += wt
                visited[node] = 1
            
            for n, wt in adj[node]:
                if visited[n] == 0:
                    heapq.heappush(q, (wt, n, node))
                    
        return mst
