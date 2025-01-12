# https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/description/

# 1. Priority Queue , heap
# BEST
# Time Complexity : O(nlogk)
# Space Complexity : O(k)
from typing import List
import heapq
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        if k==len(nums):
            return nums

        min_heap=[]
        for i,val in enumerate(nums):
            heapq.heappush(min_heap,(val,i))
            if len(min_heap)>k:
                heapq.heappop(min_heap)

        top_k=sorted(min_heap,key=lambda x:x[1])
        return [num for num,i in top_k]

    

# 2. Sorting , dictionary
# Time Complexity : O(nlogn)
# Space Complexity : O(n)
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        d={}
        ans=[]
        for i in range(len(nums)):
            d[i]=nums[i]

        sorted_dict=dict(sorted(d.items(),key=lambda item:item[1],reverse=True))

        k1=k
        dict1={}
        for index in sorted_dict:
            if k1==0:
                break

            dict1[index]=sorted_dict[index]
            k1-=1

        print(dict1)
        sorted_dict1=dict(sorted(dict1.items()))
        for i in sorted_dict1:
            ans.append(sorted_dict1[i])
            

        return ans



        


