class Solution:
    def select(self, coins, ind, amount):
        if amount == 0:
            return 0

        if ind < 0:
            return 10**5

        pick, not_pick = 10**5, 10**5
        if coins[ind] <= amount:
            pick = 1 + self.select(coins, ind, amount - coins[ind])
        not_pick = self.select(coins, ind - 1, amount)

        return min(pick, not_pick)

    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        coins.sort()

        nums = self.select(coins, n - 1, amount)

        if nums == 10**5:
            return -1
        return nums
