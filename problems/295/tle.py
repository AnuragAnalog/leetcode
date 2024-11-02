class MedianFinder:
    def __init__(self):
        self.n = 0
        self.all_nums = list()

    def addNum(self, num: int) -> None:
        heapq.heappush(self.all_nums, num)
        self.n += 1

    def findMedian(self) -> float:
        nums = list()
        median = self.n // 2

        while len(self.all_nums) != 0:
            nums.append(heapq.heappop(self.all_nums))

        for n in nums:
            heapq.heappush(self.all_nums, n)

        if self.n % 2:
            return nums[median]
        else:
            return sum(nums[median-1:median+1]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
