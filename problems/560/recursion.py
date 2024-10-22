class Solution:
    def get_sum(self, nums, ind, sum_val, k):
        if ind < 0:
            return 0

        if sum_val + nums[ind] == k:
            return 1 + self.get_sum(nums, ind - 1, sum_val + nums[ind], k)
        if sum_val + nums[ind] != k:
            return self.get_sum(nums, ind - 1, sum_val + nums[ind], k)

    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        count = 0
        for i in range(n-1, -1, -1):
            count += self.get_sum(nums, i, 0, k)

        return count
