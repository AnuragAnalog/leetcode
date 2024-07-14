class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x < 0:
            neg = True
            x = -x

        reverse = int(str(x)[::-1])

        if reverse < -2**31 or reverse > (2**31) - 1:
            return 0
        else:
            if neg:
                return -reverse
            else:
                return reverse
