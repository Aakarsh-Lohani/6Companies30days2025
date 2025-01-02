# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/description/

# Time Complexity : O(nlogn) due to sorting
# Space Complexity : O(1) temp is just reference to nums
from typing import List
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        temp=nums
        res=0
        temp.sort()
        l=len(nums)
        # m is median
        if l%2==0:
            m=(temp[l//2]+temp[(l//2)-1])//2
        else:
            m=temp[l//2]
        for i in temp:
            res+=abs(m-i)
        return res
