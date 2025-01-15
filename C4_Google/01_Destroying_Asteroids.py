# https://leetcode.com/problems/destroying-asteroids/description/

# Better Solution is possible, but this is fine too.
# Time Complexity : O(nlogn) , sorting
# Space Complexity : O(1), constant space
from typing import List

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for asteroid in asteroids:
            if asteroid > mass:
                return False
            mass += asteroid
        return True