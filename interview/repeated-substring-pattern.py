class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(len(s) - 1):
            if s.count(s[: i + 1]) * len(s[: i + 1]) == len(s):
                if s == s.count(s[: i + 1]) * s[: i + 1]:
                    return True

        return False
