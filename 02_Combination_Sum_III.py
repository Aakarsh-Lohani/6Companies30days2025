# https://leetcode.com/problems/combination-sum-iii/description/

# Time Complexity: O(9 choose k * k)
# Space Complexity: O(9 choose k * k)
from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(remain, comb, next_start):
            if remain == 0 and len(comb) == k:
                results.append(list(comb))
                return
            elif remain < 0 or len(comb) == k:
                return
            for i in range(next_start, 10):
                comb.append(i)
                backtrack(remain - i, comb, i + 1)
                comb.pop()
        results = []
        backtrack(n, [], 1)
        return results
        