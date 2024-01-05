# ========== EASY =========
# Link: https://leetcode.com/problems/the-employee-that-worked-on-the-longest-task/

class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        maxTime = 0
        hardestWorkerId = -1
        
        for i in range(len(logs)):
            employeeId, totalTimeUnits = logs[i]
            employeeTime = 0
            
            if i == 0:
                employeeTime = totalTimeUnits
            else:
                employeeTime = totalTimeUnits - logs[i - 1][1]
                
            if employeeTime > maxTime:
                maxTime = employeeTime
                hardestWorkerId = employeeId
            elif employeeTime == maxTime:
                hardestWorkerId = min(hardestWorkerId, employeeId)
                
        return hardestWorkerId