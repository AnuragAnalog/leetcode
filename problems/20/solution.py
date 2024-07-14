class Solution:
    def isValid(self, s: str) -> bool:
        pars = list()

        if len(s) == 1:
            return False

        for p in s:
            if p in ["(", "[", "{"]:
                pars.append(p)
            elif p in [")", "]", "}"]:
                if len(pars) == 0:
                    return False

                if p == ")" and pars[-1] == "(":
                    pars.pop(-1)
                elif p == "]" and pars[-1] == "[":
                    pars.pop(-1)
                elif p == "}" and pars[-1] == "{":
                    pars.pop(-1)
                else:
                    return False
        
        if len(pars) == 0:
            return True
        else:
            return False
