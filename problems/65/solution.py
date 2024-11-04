class Solution:
    def alpha_present(self, num):
        for i in range(26):
            if chr(65+i) in num or chr(97+i) in num:
                return True
        return False

    def check_number(self, num, expo=False):
        # Number has more than 1 dot or 0 incase of expo
        if expo is False and num.count(".") > 1:
            return False
        elif expo and num.count(".") > 0:
            return False

        # Alphabets
        if self.alpha_present(num):
            return False
        
        # Sign
        if ("+" != num[0] and num.count("+") > 0) or ("+" == num[0] and num.count("+") > 1):
            return False
        elif ("-" != num[0] and num.count("-") > 0) or ("-" == num[0] and num.count("-") > 1):
            return False

        if len(num) == 1 and not num.isdigit():
            return False

        for n in num:
            if n.isdigit():
                break
        else:
            return False

        return True

    def isNumber(self, s: str) -> bool:
        if s[0] == "e" or s[-1] == "e" or s[0] == "E" or s[-1] == "E":
            return False

        if ("e" in s and len(s.split("e")) != 2) or ("E" in s and len(s.split("E")) != 2):
            return False

        if "e" in s and len(s.split("e")) == 2:
            dig, expo = s.split("e")
            return self.check_number(dig) and self.check_number(expo, True)
        elif "E" in s and len(s.split("E")) == 2:
            dig, expo = s.split("E")
            return self.check_number(dig) and self.check_number(expo, True)

        return self.check_number(s)
