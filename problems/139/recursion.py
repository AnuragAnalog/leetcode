class Solution:
    def search(self, s, word_dict):
        if len(s) == 0:
            return True

        n = len(s)

        for i in range(n):
            if s[:i+1] in word_dict:
                if self.search(s[i+1:], word_dict):
                    return True

        return False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_dict = set(wordDict)
        allchars = list()
        for word in wordDict:
            allchars.extend(list(word))
        allchars = set(allchars)

        if len(set(list(s)).difference(allchars)) > 0:
            return False

        return self.search(s, word_dict)
