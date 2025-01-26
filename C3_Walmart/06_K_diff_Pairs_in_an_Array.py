# https://leetcode.com/problems/k-diff-pairs-in-an-array/description/

# Time Complexity: O(n)
# Space Complexity: O(n)
from typing import List
from collections import Counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        tot=0
        if k<0:
            return 0

        count=Counter(nums)
        for num in count:
            if k==0:
                if count[num]>1:
                    tot+=1
            else:
                if num+k in count:
                    tot+=1

        return tot
        
