# ========== EASY ==========
# Link: https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split()
        last_word = arr[-1]
        return len(last_word.strip())