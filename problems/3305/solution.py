class Solution:
    def all_vowels(self, sub):
        for c in "aeiou":
            if c not in sub:
                return False

        return True

    def consonent_count(self, sub):
        count = 0
        for s in sub:
            if s not in "aeiou":
                count += 1

        return count

    def countOfSubstrings(self, word: str, k: int) -> int:
        if self.all_vowels(word) is False:
            return 0

        n = len(word)
        count = 0
        for i in range(n):
            for j in range(i, n):
                if self.all_vowels(word[i:j+1]) and self.consonent_count(word[i:j+1]) == k:
                    count += 1

        return count
