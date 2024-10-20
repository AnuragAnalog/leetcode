class Solution:
    def climb(self, cost, ind, dp):
        if ind in [0, 1]:
            return cost[ind]

        if dp[ind] != -1:
            return dp[ind]

        dp[ind] = cost[ind] + min(self.climb(cost, ind - 2, dp), self.climb(cost, ind - 1, dp))

        return dp[ind]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1] * (n + 1)

        return min(self.climb(cost, n - 2, dp), self.climb(cost, n - 1, dp))
