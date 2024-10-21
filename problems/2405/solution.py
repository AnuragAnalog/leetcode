class Solution:
    def unique_substring(self, substr):
        return len(substr) == len(set(substr))

    def partitionString(self, s: str) -> int:
        subset = list()
        n = len(s)
        i, j = 0, 0

        while i < n:
            while self.unique_substring(s[i:j+1]) and j < n:
                j += 1
            subset.append(s[i:j])
            i = j

        return len(subset)
