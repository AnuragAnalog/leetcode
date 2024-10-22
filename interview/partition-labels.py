class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        start = 0
        parts = list()
        for i in range(len(s)):
            if set(s[i + 1 :]).intersection(set(s[start : i + 1])) == set():
                parts.append(len(s[start : i + 1]))
                start = i + 1

        return parts
