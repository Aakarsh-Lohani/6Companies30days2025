# https://leetcode.com/problems/assign-cookies/description/


# Time Complexity: O(nlogn+mlogm)
# Space Complexity: O(m+n) # Tim sort in Python
from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        satisfiedChildren,CurrCookieId=0,0

        while satisfiedChildren<len(g) and CurrCookieId<len(s):
            if s[CurrCookieId]>=g[satisfiedChildren]:
                satisfiedChildren+=1
            CurrCookieId+=1
            

        return satisfiedChildren
