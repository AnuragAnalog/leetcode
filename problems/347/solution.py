class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        topk = list()

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        for ky, v in freq.items():
            heapq.heappush(topk, (-v, ky))

        res = list()
        for _ in range(k):
            _, num = heapq.heappop(topk)
            res.append(num)

        return res
