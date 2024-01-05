# ========== EASY =========
# Link: https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # Flip the image
        for i in range(len(image)):
            start = 0
            end = len(image) - 1
            while start <= end:
                image[i][start], image[i][end] = image[i][end], image[i][start]
                start += 1
                end -= 1
        
        print(image)

        # Invert the image
        for i in range(len(image)):
            for j in range(len(image[i])):
                image[i][j] = 0 if image[i][j] == 1 else 1
        
        return image