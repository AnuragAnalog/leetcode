class Solution:
    def __init__(self):
        self.all_ips = list()

    def divide_ips(self, s, ip_str, cuts):
        if len(s) == 0:
            if cuts == 4:
                self.all_ips.append(".".join(ip_str))
            return

        if 0 <= int(s[:1]) <= 9:
            self.divide_ips(s[1:], ip_str + [s[:1]], cuts + 1)
        if 10 <= int(s[:2]) <= 99:
            self.divide_ips(s[2:], ip_str + [s[:2]], cuts + 1)
        if 100 <= int(s[:3]) <= 255:
            self.divide_ips(s[3:], ip_str + [s[:3]], cuts + 1)

    def restoreIpAddresses(self, s: str) -> List[str]:
        self.divide_ips(s, [], 0)

        return self.all_ips
