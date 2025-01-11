# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/description/

# Time Complexity : O(n)
# Space Complexity : O(k)

# Create a dictionary to store count of digits , if len(dictionary ) is k , uppdate the sum if needed. check all subarrays of len k.

from typing import List
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        d={}
        m=0
        sum1=0

        for i in range(k):
            if nums[i] in d:
                d[nums[i]]+=1
            else:
                d[nums[i]]=1
            sum1+=nums[i]

        if len(d)==k:
            m=sum1

        for j in range(k,len(nums)):
            if nums[j] in d:
                d[nums[j]]+=1
            else:
                d[nums[j]]=1

            sum1+=nums[j]
            sum1-=nums[j-k]

            d[nums[j-k]]-=1
            if d[nums[j-k]]==0:
                del d[nums[j-k]]

            # print(d)
            
            if len(d)==k:
                m=max(m,sum1)

        if m>0:
            return m
        return 0

