class Solution:
    def __init__(self):
        self.min_path = 10**5
        self.directions = list()

        for i in [1, 0, -1]:
            for j in [1, 0, -1]:
                if i == 0 and j == 0:
                    continue
                self.directions.append((i, j))

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        self.n = len(grid)

        if grid[0][0] == 1 or grid[self.n-1][self.n-1] == 1:
            return -1
    
        visited = [[0 for _ in range(self.n)] for _ in range(self.n)]
        visited[0][0] = 1

        q = [(0, 0)]
        while q:
            x, y = q.pop(0)
            if x == self.n - 1 and y == self.n - 1:
                return visited[x][y]

            for dx, dy in self.directions:
                if 0 <= x + dx < self.n and 0 <= y + dy < self.n and grid[x+dx][y+dy] == 0:
                    if visited[x+dx][y+dy] == 0:
                        q.append((x+dx, y+dy))
                        visited[x+dx][y+dy] = visited[x][y] + 1        
        return -1
