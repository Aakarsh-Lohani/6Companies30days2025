# https://leetcode.com/problems/random-flip-matrix/description/

# Check for better solution also
# Time Complexity:
# - Initialization (__init__): O(1)
# - Flipping a Cell (flip): O(1)
# - Resetting the Matrix (reset): O(1)

# Space Complexity: O(m * n)
import random

class Solution:

    def __init__(self, m: int, n: int):
        self.m, self.n = m, n
        self.total = m * n
        self.pos = {}

    def flip(self):
        r = random.randint(0, self.total - 1)
        self.total -= 1
        
        # Using Fisher-Yates shuffling algorithm
        val = self.pos.get(r, r)
        self.pos[r] = self.pos.get(self.total, self.total)
        return divmod(val, self.n)

    def reset(self):
        self.total = self.m * self.n
        self.pos = {}