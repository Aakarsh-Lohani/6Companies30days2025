# https://leetcode.com/problems/repeated-dna-sequences/description/

# Time Complexity : O(n)
# Space Complexity : O(n)

from typing import List
from collections import defaultdict

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        
        sequences = defaultdict(int)
        for i in range(len(s) - 9):
            sequences[s[i:i+10]] += 1
            
        return [seq for seq, freq in sequences.items() if freq > 1]