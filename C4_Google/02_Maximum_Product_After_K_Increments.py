# https://leetcode.com/problems/maximum-product-after-k-increments/description/

# Time Complexity : O(n+klogn)
# Space Complexity : O(n)
import heapq
from typing import List
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        # Need to increment minimum number in list at each operation
        prod=1
        min_heap=nums.copy()  
        heapq.heapify(min_heap)  # O(n)

        for i in range(k):  #O(klogn)
            num=heapq.heappop(min_heap)
            heapq.heappush(min_heap,num+1)  

        for n in min_heap:
            prod=(prod*n)%(10**9+7)

        return prod