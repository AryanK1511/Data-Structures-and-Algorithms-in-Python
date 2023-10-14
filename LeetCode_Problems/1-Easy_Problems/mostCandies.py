# ========== EASY =========
# Link: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        output = []
        max_candies = max(candies)
        for i in range(len(candies)):
            if (candies[i] + extraCandies) >= max_candies:
                output.append(True)
            else:
                output.append(False)
        return output

