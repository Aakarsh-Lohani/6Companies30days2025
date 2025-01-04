# https://leetcode.com/problems/wiggle-sort-ii/description/

# Time Complexity: (O(nlogn)) due to inplace sorting
# Space Complexity: (O(n)) due to space required for slicing, which create new lists
from typing import List
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        h=len(nums[::2])
        nums[::2],nums[1::2]=nums[:h][::-1],nums[h:][::-1]
        
