class Solution:
    def roll(self, n, k, target, dp):
        if target < 0:
            return 0
        if n < 0:
            return 0
        if target == 0 and n == 0:
            return 1
        elif target == 0 or n == 0:
            return 0

        if dp[target][n] != -1:
            return dp[target][n]

        count = 0
        for i in range(1, k + 1):
            count += self.roll(n-1, k, target - i, dp)

        dp[target][n] = count

        return dp[target][n]

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[0 for _ in range(n+1)] for _ in range(target+1)]
        for i in range(n+1):
            dp[0][i] = 0

        for j in range(target+1):
            dp[j][0] = 0

        dp[0][0] = 1

        for i in range(1, target+1):
            for j in range(1, n+1):
                count = 0
                for m in range(1, k + 1):
                    if m <= i:
                        count += dp[i - m][j - 1]

                dp[i][j] = count % (10**9 + 7)
 
        return dp[target][n] % (10**9 + 7)
