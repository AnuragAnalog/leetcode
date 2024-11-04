class Solution:
    def coefficients(self, equation):
        a, b = 0, 0
        for value in equation.split("+"):
            if value == "":
                continue
            if value[-1] == "x":
                if value[:-1] == "":
                    a += 1
                elif value[:-1] == "-":
                    a -= 1
                else:
                    a += int(value[:-1])
            else:
                b += int(value)

        return a, b

    def solveEquation(self, equation: str) -> str:
        new_equation = ""
        for e in equation:
            if e == "-":
                new_equation += "+"
            new_equation += e

        lhs, rhs = new_equation.split("=")
        print(lhs.split("+"), rhs.split("+"))
        a, b = self.coefficients(lhs)
        c, d = self.coefficients(rhs)

        if a == c:
            if b == d:
                return "Infinite solutions"
            else:
                return "No solution"

        return f"x={(d - b)//(a - c)}"
