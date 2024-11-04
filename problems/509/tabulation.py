class Solution:
    def fib(self, n: int) -> int:
        if n in [0, 1]:
            return n

        fibs = [-1] * (n + 1)
        fibs[0] = 0
        fibs[1] = 1

        for i in range(2, n+1):
            fibs[i] = fibs[i-1] + fibs[i-2]

        return fibs[n]
