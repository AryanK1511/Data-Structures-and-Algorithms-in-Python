# ========== EASY =========
# Link: https://leetcode.com/problems/summary-ranges/description/

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        summaries = []
        index = 0
        while index < len(nums):
            range_arr = [nums[index]]
            while index < len(nums) - 1 and nums[index] + 1 == nums[index + 1]:
                index += 1
            if range_arr[-1] != nums[index]:
                range_arr.append(nums[index])
            index += 1
            if len(range_arr) == 1:
                summaries.append(str(range_arr[0]))
            else:
                summaries.append(f"{range_arr[0]}->{range_arr[-1]}")
        return summaries
