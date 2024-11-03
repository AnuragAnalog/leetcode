class Solution:
    def __init__(self):
        self.min_path = 10**5
        self.directions = list()

        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i == 0 and j == 0:
                    continue
                self.directions.append((i, j))

    def path(self, grid, x, y, visited, path_len):
        if grid[x][y] == 0:
            path_len += 1
        else:
            return
        if x == self.n - 1 and y == self.n - 1:
            self.min_path = min(self.min_path, path_len)
            return

        if visited[x][y]:
            return

        visited[x][y] = 1
        for dx, dy in self.directions:
            if 0 <= x + dx < self.n and 0 <= y + dy < self.n:
                self.path(grid, x+dx, y+dy, visited, path_len)
        visited[x][y] = 0

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        self.n = len(grid)
        visited = [[0 for _ in range(self.n)] for _ in range(self.n)]

        self.path(grid, 0, 0, visited, 0)

        if self.min_path == 10**5:
            return -1
        return self.min_path
