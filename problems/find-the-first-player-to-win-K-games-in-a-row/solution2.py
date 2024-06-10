class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        i = 0
        curr = 0
        n = len(skills)

        for j in range(1, n):
            if skills[i] < skills[j]:
                curr = 0
                i = j
            curr += 1

            if curr == k:
                break

        return i
