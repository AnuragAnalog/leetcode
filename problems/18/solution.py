class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        quads = list()

        snums = sorted(nums)

        for i in range(n):
            for j in range(i + 1, n):
                k = j + 1
                l = n - 1

                while k < l:
                    sum_val = snums[i] + snums[j] + snums[k] + snums[l]
                    if sum_val == target:
                        v = sorted([snums[i], snums[j], snums[k], snums[l]])
                        if v not in quads:
                            quads.append(v)
                        k += 1
                        l -= 1
                    elif sum_val < target:
                        k += 1
                    elif sum_val > target:
                        l -= 1

        return quads
