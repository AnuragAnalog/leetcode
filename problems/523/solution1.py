class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        for i in range(n-1):
            check_sum = nums[i]
            for j in range(i+1, n):
                if (check_sum + nums[j]) % k == 0:
                    return True
                check_sum += nums[j]

        return False
