class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        wins = dict()
        positions = [i for i in range(len(skills))]

        while k not in wins.values():
            p1, p2 = positions[0], positions[1]
            if skills[p1] > skills[p2]:
                wins[skills[p1]] = wins.get(skills[p1], 0) + 1
                lose = positions.pop(1)
                positions.append(lose) 
            else:
                wins[skills[p2]] = wins.get(skills[p2], 0) + 1
                lose = positions.pop(0)
                positions.append(lose)

        for ky, vl in wins.items():
            if vl == k:
                return skills.index(ky)
