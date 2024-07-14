class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_word = min(strs, key=lambda x: len(x))

        ans = ""
        for i in range(len(min_word)):
            count = 0
            for j in range(len(strs)):
                if strs[j][i] == min_word[i]:
                    count += 1

            if count == len(strs):
                ans += min_word[i]
            else:
                break

        return ans
