# ========== EASY =========
# Link: https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/description/

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        count = 0
        for i in range(len(seats)):
            count += abs(seats[i]-students[i])
        return count