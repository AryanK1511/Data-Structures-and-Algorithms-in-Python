# ========== EASY ==========
# Link: https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        romanNumbers = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        ans = 0
        for i in range(len(s)):
            if (i < len(s) - 1 and romanNumbers[s[i]] < romanNumbers[s[i + 1]]):
                ans -= romanNumbers[s[i]]
            else:
                ans += romanNumbers[s[i]]

        return ans
        