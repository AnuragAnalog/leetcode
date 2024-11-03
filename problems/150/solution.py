class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()

        for t in tokens:
            if t.isdigit() or t[1:].isdigit():
                stack.append(int(t))
            elif t in ["+", "-", "*", "/"]:
                b = stack.pop()
                a = stack.pop()
                res = int(eval(f"{a}{t}{b}"))
                stack.append(res)

        return stack[-1]
