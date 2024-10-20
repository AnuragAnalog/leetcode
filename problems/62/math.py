class Solution:
    def factorial(self, n):
        val = 1
        for i in range(1, n+1):
            val *= i

        return val

    def uniquePaths(self, m: int, n: int) -> int:
        mn_fac = self.factorial(m + n - 2)
        m_fac = self.factorial(m - 1)
        n_fac = self.factorial(n - 1)

        return int(mn_fac / (m_fac * n_fac))
