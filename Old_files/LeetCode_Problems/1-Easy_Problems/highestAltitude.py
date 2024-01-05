# ========== EASY =========
# Link: https://leetcode.com/problems/find-the-highest-altitude/

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        gain.insert(0, 0)
        relative_height = 0
        max_val = 0
        for i in range(len(gain) - 1):
            relative_height += gain[i + 1]
            max_val = max(relative_height, max_val)
        return max_val