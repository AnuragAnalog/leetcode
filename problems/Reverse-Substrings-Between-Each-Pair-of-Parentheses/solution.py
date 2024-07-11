class Solution:
    def reverseParentheses(self, s: str) -> str:
        letter_stack = list()

        for c in s:
            if c == ")":
                rev = ""
                while len(letter_stack) != 0 and letter_stack[-1] != "(":
                    rev += letter_stack.pop()

                if len(letter_stack) != 0:
                    letter_stack.pop()
                
                for cc in rev:
                    letter_stack.append(cc)
            else:
                letter_stack.append(c)

        return "".join(letter_stack)
