class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Binary Exponential
        final = x
        neg = False

        if n == 0:
            return 1

        if n < 0:
            n = -1 * n
            neg = True

        bins = ""
        while n != 0:
            bins += str(n & 1)
            n = n >> 1

        for dig in bins[::-1][1:]:
            final *= final
            if dig == "1":
                final *= x

        if neg:
            return 1 / final
        return final
