class Solution:
    def satisfaction(self, satisfy, ind, num_dish):
        if len(satisfy) == ind:
            return 0

        if self.dp[ind][num_dish] != -1:
            return self.dp[ind][num_dish]

        self.dp[ind][num_dish] = max(satisfy[ind]*(num_dish+1) + self.satisfaction(satisfy, ind+1, num_dish+1), self.satisfaction(satisfy, ind+1, num_dish))

        return self.dp[ind][num_dish]

    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        n = len(satisfaction)
        self.dp = [[-1 for _ in range(n+1)] for _ in range(n)]
        satisfaction.sort()
        self.satisfaction(satisfaction, 0, 0)

        return max(0, self.dp[0][0])
