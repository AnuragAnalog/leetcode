class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        n = len(coins)
        coins.sort()

        dp = [[10**5 for _ in range(amount+1)] for _ in range(n)]

        for a in range(amount+1):
            if a % coins[0] == 0:
                dp[0][a] = a // coins[0]

        for ind in range(1, n):
            for a in range(amount+1):
                pick, not_pick = 10**5, 10**5
                if coins[ind] <= a:
                    pick = 1 + dp[ind][a - coins[ind]]
                not_pick = dp[ind - 1][a]

                dp[ind][a] = min(pick, not_pick)

        if dp[n-1][amount] == 10**5:
            return -1
        return dp[n-1][amount]
