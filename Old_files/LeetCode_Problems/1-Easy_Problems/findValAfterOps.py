# ========== EASY =========
# Link: https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X = 0
        for i in range(len(operations)):
            for j in range(len(operations[i])):
                if operations[i][j] != 'X':
                    X += int(operations[i][j] + str(1))
                    break
        return X