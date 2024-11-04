class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = list()

        for i, num in enumerate(nums):
            if i == 0:
                prefix.append(num)
                continue
            prefix.append(prefix[-1] + num)

        prefix_map = dict()

        count = 0
        for ps in prefix:
            if ps == k:
                count += 1
            if ps - k in prefix_map:
                count += prefix_map[ps - k]
            prefix_map[ps] = prefix_map.get(ps, 0) + 1

        return count
