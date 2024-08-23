class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_h = sorted(heights)

        return sum([True for x, y in zip(sorted_h, heights) if x != y])
