class Solution:
    def rob_house(self, houses, ind):
        if ind == 0:
            return houses[ind]

        value1, value2 = 0, 0
        if ind > 1:
            value2 = houses[ind] + self.rob_house(houses, ind - 2)
        value1 = max(houses[ind], self.rob_house(houses, ind - 1))

        return max(value1, value2)

    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        return self.rob_house(nums, n - 1)
