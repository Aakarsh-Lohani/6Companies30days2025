# https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/description/

# Time Complexity: O(n^2*4^n)
# Space Complexity: O(n)
from itertools import combinations
class Solution:
    def maxProduct(self, s: str) -> int:
        def is_palindrome(s: str) -> bool:
            return s == s[::-1]

        n = len(s)
        max_product = 0
        for i in range(1<<n):
            t = [j for j in range(n) if (i>>j)&1]
            sub_strs = [s[j] for j in t]
            if is_palindrome(sub_strs):
                rest_strs = [s[j] for j in range(n) if j not in t]
                for x in range(1, len(rest_strs) + 1):
                    for sub in combinations(rest_strs, x):
                        if is_palindrome(sub):
                            max_product = max(max_product, len(sub_strs) * len(sub))
        return max_product