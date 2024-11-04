class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        new_arr = [-1] * n

        for num in nums:
            if num <= 0 or num - 1 >= n:
                continue
            else:
                new_arr[num - 1] = 1

        for i, na in enumerate(new_arr):
            if na == -1:
                return i + 1

        return n + 1
