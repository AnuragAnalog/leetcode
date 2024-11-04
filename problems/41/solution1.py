class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()

        count = 1
        for num in nums:
            if num <= 0:
                continue
            if count != num:
                return count

            count += 1

        return count
