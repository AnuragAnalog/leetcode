class Solution:
    def any_fresh(self, grid):
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return True

        return False

    def rot_it(self, grid, visited, indices):
        change = False
        for i, j in indices:
            if 0 <= i + 1 < self.m and 0 <= j < self.n and grid[i + 1][j] == 1:
                change = True
                grid[i + 1][j] = 2
            if 0 <= i - 1 < self.m and 0 <= j < self.n and grid[i - 1][j] == 1:
                change = True
                grid[i - 1][j] = 2
            if 0 <= i < self.m and 0 <= j + 1 < self.n and grid[i][j + 1] == 1:
                change = True
                grid[i][j + 1] = 2
            if 0 <= i < self.m and 0 <= j - 1 < self.n and grid[i][j - 1] == 1:
                change = True
                grid[i][j - 1] = 2

        return grid, change

    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        visited = [[0 for _ in range(self.n)] for _ in range(self.m)]

        if self.any_fresh(grid) is False:
            return 0

        t = 0

        while self.any_fresh(grid):
            indices = set()
            for i in range(self.m):
                for j in range(self.n):
                    if visited[i][j] == 0 and grid[i][j] == 2:
                        visited[i][j] = 1
                        indices.add((i, j))
            grid, change = self.rot_it(grid, visited, indices)
            if change is False:
                break

            t += 1

        if self.any_fresh(grid):
            return -1

        return t
