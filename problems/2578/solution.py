class Solution:
    def splitNum(self, num: int) -> int:
        num_list = sorted(list(str(num)))
        n = len(num_list)

        num1, num2 = "", ""
        for i in range(0, n, 2):
            num1 += str(num_list[i])
            if i + 1 < n:
                num2 += str(num_list[i + 1])

        return int(num1) + int(num2)
