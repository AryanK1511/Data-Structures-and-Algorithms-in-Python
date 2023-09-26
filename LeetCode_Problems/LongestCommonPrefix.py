# Link: https://leetcode.com/problems/longest-common-prefix/description/
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        longestCommonPrefix = ""
        firstWord = strs[0]
        
        for i in range(len(firstWord)):
            char = firstWord[i]
            for word in strs[1:]:
                if i >= len(word) or word[i] != char:
                    return longestCommonPrefix
            longestCommonPrefix += char
            
        return longestCommonPrefix