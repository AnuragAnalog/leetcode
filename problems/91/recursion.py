class Solution:
    def decode(self, s):
        if len(s) == 0:
            return 1

        if s[0] == "0":
            return 0

        count = self.decode(s[1:])
        if len(s) > 1 and s[:2] < "27":
            count += self.decode(s[2:])

        return count

    def numDecodings(self, s: str) -> int:
        return self.decode(s)
