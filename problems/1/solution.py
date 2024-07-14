class Solution:
    def binarySearch(self, nums, value) -> int:
        i = 0
        j = len(nums) - 1

        while i <= j:
            mid = (i + j) // 2

            if nums[mid][0] == value:
                return nums[mid][1]
            elif value > nums[mid][0]:
                i = mid + 1
            elif value < nums[mid][0]:
                j = mid - 1

        return -1

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        sorted_nums = list(map(list, sorted(zip(nums, range(n)), key=lambda x: x[0])))

        for i, snum in enumerate(sorted_nums):
            fval = sorted_nums[i][0]
            sorted_nums[i][0] = 10**30
            sval = self.binarySearch(sorted_nums, target-fval)
            if sval != -1:
                print(sval)
                return [sorted_nums[i][1], sval]
            sorted_nums[i][0] = fval
