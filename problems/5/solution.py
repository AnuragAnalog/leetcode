class Solution:
    def palindrome(self, s) -> str:
        return s == s[::-1]

    def longestPalindrome(self, s: str) -> str:
        maxi_str = ""
        maxi = 0
        n = len(s)

        if n == 1:
            return s

        for i in range(n):
            for j in range(i + 1, n + 1):
                if self.palindrome(s[i:j]):
                    if maxi < len(s[i:j]):
                        maxi = len(s[i:j])
                        maxi_str = s[i:j]

        return maxi_str
