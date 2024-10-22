class Solution:
    def robHouses(self, houses):
        n = len(houses)
        value = [0] * len(houses)
        value[0] = houses[0]
        value[1] = max(houses[0], houses[1])

        for i in range(2, n):
            value[i] = max(houses[i] + value[i - 2], value[i - 1])

        return value[-1]

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)

        n = len(nums)
        return max(self.robHouses(nums[1:]), self.robHouses(nums[:-1]))
