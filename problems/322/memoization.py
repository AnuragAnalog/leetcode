class Solution:
    def select(self, coins, ind, amount, dp):
        if amount == 0:
            return 0

        if ind < 0:
            return 10**5

        if dp[ind][amount] != -1:
            return dp[ind][amount]

        pick, not_pick = 10**5, 10**5
        if coins[ind] <= amount:
            pick = 1 + self.select(coins, ind, amount - coins[ind], dp)
        not_pick = self.select(coins, ind - 1, amount, dp)

        dp[ind][amount] = min(pick, not_pick)

        return dp[ind][amount]

    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        coins.sort()

        dp = [[-1 for _ in range(amount+1)] for _ in range(n)]

        nums = self.select(coins, n - 1, amount, dp)

        if nums == 10**5:
            return -1
        return nums
