class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        rev_number = 0
        ox = x

        while x != 0:
            rev_number = rev_number * 10 + x % 10
            x = int(x // 10)

        if ox == rev_number:
            return True
        else:
            return False
