class Solution:
    def numTrees(self, n: int) -> int:
        if n in [0, 1]:
            return 1

        total = 0
        for i in range(1, n+1):
            total += (self.numTrees(i-1) * self.numTrees(n - i))

        return total
