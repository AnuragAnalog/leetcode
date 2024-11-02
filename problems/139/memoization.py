class Solution:
    def search(self, s, word_dict, dp, start):
        if len(s[start:]) == 0:
            return True

        if dp[start] != -1:
            return dp[start]

        for word in word_dict:
            if s[start:].startswith(word):
                if self.search(s, word_dict, dp, start+len(word)):
                    dp[start] = True
                    return dp[start]

        dp[start] = False
        return dp[start]

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_dict = set(wordDict)
        dp = [-1] * len(s)

        return self.search(s, wordDict, dp, 0)
