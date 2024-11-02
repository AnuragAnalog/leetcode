class MedianFinder:
    def __init__(self):
        self.h1 = list()
        self.h2 = list()

    def addNum(self, num: int) -> None:
        if len(self.h1) + len(self.h2) == 0:
            heapq.heappush(self.h2, num)
            return

        if num < self.h2[0]:
            heapq.heappush(self.h1, -num)
        else:
            heapq.heappush(self.h2, num)
        
        if len(self.h2) > len(self.h1) + 1:
            heapq.heappush(self.h1, -heapq.heappop(self.h2))
        elif len(self.h1) > len(self.h2) + 1:
            heapq.heappush(self.h2, -heapq.heappop(self.h1))

    def findMedian(self) -> float:
        if len(self.h1) > len(self.h2):
            return -self.h1[0]
        elif len(self.h1) < len(self.h2):
            return self.h2[0]
        else:
            return (self.h2[0]-self.h1[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
