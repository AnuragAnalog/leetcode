class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        count0 = 0
        count1 = 0
        count2 = 0

        for n in nums:
            if n == 0:
                count0 += 1
            elif n == 1:
                count1 += 1
            elif n == 2:
                count2 += 1
        
        for i in range(count0):
            nums[i] = 0
        for i in range(count1):
            nums[count0+i] = 1
        for i in range(count2):
            nums[count0+count1+i] = 2

        return nums
