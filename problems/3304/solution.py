class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        while len(word) <= k:    
            changed = "".join(map(lambda x: chr(((ord(x) - 96) % 26) + 97), word))
            word += changed

        return word[k - 1]
