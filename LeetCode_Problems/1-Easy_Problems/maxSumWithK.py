# ========== EASY =========
# Link: https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/?source=submission-noac

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        sum = 0
        for i in range(k):
            last_element = nums.pop()
            sum += last_element
            nums.append(last_element + 1)

        return sum