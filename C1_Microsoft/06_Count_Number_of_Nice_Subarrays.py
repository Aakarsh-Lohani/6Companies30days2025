# https://leetcode.com/problems/count-number-of-nice-subarrays/description/

# Time Complexity : O(n)
# Space Complexity : O(n)
from typing import List
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        res = 0
        prefix = [0] * (len(nums) + 1)
        prefix[0] = 1
        for num in nums:
            count += num & 1
            prefix[count] += 1
            if count >= k:
                res += prefix[count - k]
        return res