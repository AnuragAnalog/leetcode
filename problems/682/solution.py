class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = list()

        for oper in operations:
            if oper.isdigit() or oper[1:].isdigit():
                scores.append(int(oper))
            elif oper == "C":
                scores.pop()
            elif oper == "D":
                scores.append(scores[-1] * 2)
            elif oper == "+":
                scores.append(sum(scores[-2:]))

        return sum(scores)
