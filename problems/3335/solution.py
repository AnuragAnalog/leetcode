class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        freq = [0] * 26

        for c in s:
            freq[ord(c)-97] += 1

        for _ in range(t):
            temp = freq[-1]
            freq = [temp] + freq[:-1]
            freq[1] += freq[0]

        return sum(freq) % (10**9 + 7)
