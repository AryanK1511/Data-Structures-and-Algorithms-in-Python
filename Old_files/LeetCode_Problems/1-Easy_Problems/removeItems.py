# ========== EASY ==========
# Link: https://leetcode.com/problems/remove-element/ 

class Solution:
    def removeElement(self, nums, val):
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index