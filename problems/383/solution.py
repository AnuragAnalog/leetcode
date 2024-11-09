class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_freq, mag_freq = dict(), dict()

        for r in ransomNote:
            ransom_freq[r] = ransom_freq.get(r, 0) + 1

        for m in magazine:
            mag_freq[m] = mag_freq.get(m, 0) + 1

        for k, v in ransom_freq.items():
            if mag_freq.get(k, 0) < v:
                return False

        return True
