# ========== EASY =========
# Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            lenCount = 0
            for j in range(len(needle)):
                if haystack[i + j] == needle[j]:
                    lenCount += 1
            if lenCount == len(needle):
                return i
        return -1