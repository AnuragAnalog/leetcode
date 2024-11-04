class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)

        for i in range(n):
            total = nums[i]
            count += int(total == k)

            for j in range(i + 1, n):
                total += nums[j]
                count += int(total == k)

        return count
