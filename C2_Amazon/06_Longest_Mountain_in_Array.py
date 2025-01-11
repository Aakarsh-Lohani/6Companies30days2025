# https://leetcode.com/problems/longest-mountain-in-array/description/

# Other possible approaches: Dynamic Programming, Enumeration
# 1. Two pointer
# Time Complexity: O(n)
# Space Complexity: O(1)
from typing import List
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        N=len(arr)

        base,res=0,0

        while base<N:
            end=base
            if end+1<N and arr[end]<arr[end+1]:
                while end+1<N and arr[end]<arr[end+1]:
                    end+=1

                # At peak                
                if end+1<N and arr[end]>arr[end+1]:
                    while end+1<N and arr[end]>arr[end+1]:
                        end+=1

                    res=max(end-base+1,res)
            base=max(end,base+1)
        return res
    