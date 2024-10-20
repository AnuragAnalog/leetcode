class Solution:
    def satisfaction(self, satisfy, ind, num_dish):
        if len(satisfy) == ind:
            return 0

        return max(satisfy[ind]*num_dish + self.satisfaction(satisfy, ind+1, num_dish+1), self.satisfaction(satisfy, ind+1, num_dish))

    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        max_satisfy = 0
        satisfaction.sort()

        return max(0, self.satisfaction(satisfaction, 0, 1))
