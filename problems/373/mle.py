class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pairs = dict()

        for n1 in nums1:
            for n2 in nums2:
                if n1 + n2 not in pairs:
                    pairs[n1 + n2] = list()
                pairs[n1 + n2].append([n1, n2])

        res = list()
        sorted_pairs = sorted(pairs.items(), key=lambda x: x[0])

        for _, pairs in sorted_pairs:
            if len(pairs) <= k:
                res.extend(pairs)
                k -= len(pairs)
            else:
                res.extend(pairs[:k])
                k = 0
                break

        return res
