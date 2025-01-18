# https://leetcode.com/problems/kth-largest-element-in-a-stream/description/

# Time Complexity: O((M+N)logk)
# Let M be the size of the initial stream nums given in the constructor, and let N be the number of calls to add
# Space Complexity : O(k)
import heapq
from typing import List
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.min_heap=nums
        heapq.heapify(self.min_heap)
        while len(self.min_heap)>k:
            heapq.heappop(self.min_heap)        

    def add(self, val: int) -> int:
        if len(self.min_heap)<self.k:
            heapq.heappush(self.min_heap,val)
        elif val>self.min_heap[0]:
            heapq.heapreplace(self.min_heap,val)
        return self.min_heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)