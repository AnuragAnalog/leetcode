class Solution:
    def decode(self, s, dp, ind):
        if len(s) == ind:
            return 1

        if s[ind] == "0":
            return 0

        if dp[ind] != -1:
            return dp[ind]

        dp[ind] = self.decode(s, dp, ind+1)
        if ind + 2 <= len(s) and s[ind:ind+2] < "27":
            dp[ind] += self.decode(s, dp, ind+2)

        return dp[ind]

    def numDecodings(self, s: str) -> int:
        dp = [-1] * len(s)

        return self.decode(s, dp, 0)
