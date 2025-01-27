# https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/description/

# Time Complexity: O(log(min(divisor1, divisor2)))
# Space Complexity: O(1)
import math
class Solution:

    def calculateLCM(self, a, b):
        return (a * b) // math.gcd(a, b)

    def calculateMax(self, count, divisor1, divisor2=1):
        lcm_result = self.calculateLCM(divisor1, divisor2)
        return count + count // (lcm_result - 1) - (0 if count % (lcm_result - 1) else 1)

    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        return max(
            self.calculateMax(uniqueCnt1, divisor1),
            self.calculateMax(uniqueCnt2, divisor2),
            self.calculateMax(uniqueCnt1 + uniqueCnt2, divisor1, divisor2)
        )
