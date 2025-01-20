# https://leetcode.com/problems/count-words-obtained-after-adding-a-letter/description/

# Better solution possible using Bitmask
# Time Complexity: O(n*L+m*L^2)
# Space Complexity: O(n*L)
from collections import Counter
from typing import List
class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        startWords = Counter(frozenset(word) for word in startWords)
        count = 0
        for target in targetWords:
            targetSet = frozenset(target)
            for ch in targetSet:
                if targetSet - {ch} in startWords:
                    count += 1
                    break
        return count
