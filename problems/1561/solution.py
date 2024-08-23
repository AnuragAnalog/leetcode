class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        mid = n // 2
        mid_val = nums[mid]

        moves = 0
        for num in nums:
            moves += abs(num - mid_val)

        return moves
