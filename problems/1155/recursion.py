class Solution:
    def roll(self, n, k, target):
        if target < 0:
            return 0
        if n < 0:
            return 0
        if target == 0 and n == 0:
            return 1
        elif target == 0 or n == 0:
            return 0

        count = 0
        for i in range(1, k + 1):
            count += self.roll(n-1, k, target - i)

        return count

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        return self.roll(n, k, target) % (10**9 + 7)
