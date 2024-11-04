class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = list()
        if len(nums) == 0:
            return []
        n = len(nums)

        curr = nums[0]
        for i in range(1, n):
            if nums[i-1] == nums[i] - 1:
                continue
            else:
                res.append(f"{curr}->{nums[i-1]}")
                curr = nums[i]

        res.append(f"{curr}->{nums[-1]}")

        for i, ran in enumerate(res):
            l, r = ran.split("->")
            if int(l) == int(r):
                res[i] = l
        return res
