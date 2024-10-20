class Solution:
    def rob_house(self, houses, ind, dp):
        if ind == 0:
            return houses[ind]

        if dp[ind] != -1:
            return dp[ind]

        value1, value2 = 0, 0
        if ind > 1:
            value2 = houses[ind] + self.rob_house(houses, ind - 2, dp)
        value1 = max(houses[ind], self.rob_house(houses, ind - 1, dp))

        dp[ind] = max(value1, value2)

        return dp[ind]

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * (n + 1)

        return self.rob_house(nums, n - 1, dp)
