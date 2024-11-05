class Solution:
    def minChanges(self, s: str) -> int:
        change = 0
        curr = s[0]

        for i in range(1, len(s)):
            if curr == s[i]:
                curr += s[i]
            else:
                if len(curr) % 2:
                    change += 1
                    curr = curr[-1] + s[i]
                else:
                    curr = s[i]

        return change
