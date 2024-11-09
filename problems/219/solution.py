class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        nums_index = sorted(zip(nums, range(n)))

        for i in range(n - 1):
            if nums_index[i][0] == nums_index[i+1][0]:
                if abs(nums_index[i][1] - nums_index[i+1][1]) <= k:
                    return True

        return False
