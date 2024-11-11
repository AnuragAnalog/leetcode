class Solution:
    def product(self, array):
        prod = 1

        for a in array:
            if a == 0:
                return 0
            prod *= a

        return prod

    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            arr = list(map(int, list(str(n))))

            if self.product(arr) % t == 0:
                return n
            n += 1
