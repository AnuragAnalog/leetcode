class Solution:
    def climb(self, cost, ind):
        if ind in [0, 1]:
            return cost[ind]

        return cost[ind] + min(self.climb(cost, ind - 2), self.climb(cost, ind - 1))

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        return min(self.climb(cost, n - 2), self.climb(cost, n - 1))
