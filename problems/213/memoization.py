class Solution:
    def dp(self, ind, arr):
        if ind == 0:
            return arr[0]
        elif ind == 1:
            return max(arr[0], arr[1])
        else:
            m1 = arr[ind] + self.dp(ind - 2, arr)
            m2 = self.dp(ind - 1, arr)

        return max(m1, m2)

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)

        n = len(nums)
        return max(self.dp(n - 2, nums[1:]), self.dp(n - 2, nums[:-1]))
