# https://leetcode.com/problems/maximum-length-of-repeated-subarray/description/


# CHECK ROLLING HASH SOLUTION TOO
# Time Complexity : O(m*n)
# Space Complexity :O(m*n)
# DYNAMIC PROGRAMMING
from typing import List
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        A,B=nums1,nums2
        memo = [[0] * (len(B) + 1) for i in range(len(A) + 1)]
        for i in range(len(A) - 1, -1, -1):
            for j in range(len(B) - 1, -1, -1):
                if A[i] == B[j]:
                    memo[i][j] = memo[i + 1][j + 1] + 1
        return max(max(row) for row in memo)