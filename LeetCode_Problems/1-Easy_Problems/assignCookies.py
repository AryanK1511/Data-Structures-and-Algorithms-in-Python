# ========== EASY =========
# Link: https://leetcode.com/problems/assign-cookies/description/

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        satisfied_children = 0
        g.sort(reverse=True)
        s.sort(reverse=True)
        for greed in g:
            if len(s) == 0:
                return satisfied_children
            if greed <= s[0]:
                satisfied_children += 1
                s.pop(0)
        return satisfied_children