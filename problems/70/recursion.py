class Solution:
    def climb(self, n):
        if n == 0:
            return 1
        v1, v2 = 0, 0
        v1 = self.climb(n - 1)
        if n > 1:
            v2 = self.climb(n - 2)
        return v1 + v2

    def climbStairs(self, n: int) -> int:
        return self.climb(n)
