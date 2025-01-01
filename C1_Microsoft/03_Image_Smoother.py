# https://leetcode.com/problems/image-smoother/description/

# Time Complexity: O(m*n)
# Space Complexity: O(m*n)
from typing import List
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        res = [[0] * n for p in range(m)]

        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        for i in range(m):
            for j in range(n):
                count = 0
                total = 0
                for dr, dc in directions:
                    r, c = i + dr, j + dc
                    if 0 <= r < m and 0 <= c < n:
                        total += img[r][c]
                        count += 1
                res[i][j] = total // count
        
        return res