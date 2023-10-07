# ========== EASY =========
# Link: https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2
            if (nums[mid] > target):
                end = mid - 1
            elif (nums[mid] < target):
                start = mid + 1
            else:
                return mid
        
        return start