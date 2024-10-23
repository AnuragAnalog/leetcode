#User function Template for python3

import sys
from typing import List
sys.setrecursionlimit(10**8)
class Solution:
    def subtract_base(self, nodes, base):
        for i, node in enumerate(nodes):
            node[0] -= base[0]
            node[1] -= base[1]
            nodes[i] = node
            
        return nodes
    
    def bfs(self, grid, i, j, nodes, visited):
        m, n = len(grid), len(grid[0])
        q = [(i, j)]
        
        while q:
            node = q.pop(0)
            if visited[node[0]][node[1]] == 1:
                continue
            nodes.append(list(node))
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                del_i, del_j = node[0] + di, node[1] + dj
                if del_i in range(0, m) and del_j in range(0, n) and grid[del_i][del_j]:
                    q.append((del_i, del_j))
            visited[node[0]][node[1]] = 1
                    
        return nodes
            

    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[0 for _ in range(n)] for _ in range(m)] 
        unique_islands = set()
        
        for i in range(m):
            for j in range(n):
                if visited[i][j] != 1 and grid[i][j] == 1:
                    nodes = list()
                    nodes = self.bfs(grid, i, j, nodes, visited)
                    nodes = self.subtract_base(nodes, (i, j))
                    if len(nodes) != 0:
                        unique_islands.add(str(nodes).strip('[]'))
                    
        return len(unique_islands)
