class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 2:
            return min(height) * 1

        n = len(height)
        l, r = 0, n - 1
        maxi = 0

        while l < r:
            h = min(height[l], height[r])
            w = abs(l - r)

            if maxi < h * w:
                maxi = h * w

            if height[l] < height[r]:
                l = l + 1
            else:
                r = r - 1

        return maxi
