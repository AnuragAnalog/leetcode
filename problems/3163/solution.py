class Solution:
    def compressedString(self, word: str) -> str:
        res = ""
        n = len(word)

        count = 0
        for i, w in enumerate(word):
            if i == 0:
                count += 1
                stack = [[count, w]]
                continue
            if stack[-1][1] == w and stack[-1][0] < 9:
                stack[-1][0] += 1
            else:
                count = 1
                stack.append([count, w])

        return "".join([f"{c}{w}" for c, w in stack])
