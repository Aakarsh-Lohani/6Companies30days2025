# https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/description/

# Time Complexity :O(N∗Log(N)+M∗Log(M))
# Space Complexity :O(N+M)

from itertools import pairwise
from typing import List
class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:

        def find_max(bars):
            bars.sort()
            s = ''.join([str(int(y - x == 1)) for x,y in pairwise(bars)])
            return max(map(len,s.split('0')))+2
            
        return pow(min(find_max(hBars), find_max(vBars)),2)

# Similar way
# https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/solutions/4328944/i-hate-the-description
class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def findLongestConsecutiveElements(numsSet):
            res = 1
            for num in numsSet:
                count = 1
                current = num
                while current+1 in numsSet:
                    current += 1
                    count += 1
                res = max(res, count)
            return res
            
        res = 1
        if len(hBars) == 0 or len(vBars) == 0: return 1
        hSet, vSet = set(hBars), set(vBars)
        maxHBars, maxVBars = findLongestConsecutiveElements(hSet), findLongestConsecutiveElements(vSet)
        return (min(maxHBars, maxVBars) + 1) ** 2