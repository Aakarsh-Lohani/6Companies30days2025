# https://leetcode.com/problems/get-equal-substrings-within-budget/description/

# Sliding Window
# Time Complexity : O(n)
# Space Complexity : O(1)
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        maxLen=0

        left,right=0,0
        currCost=0
        for right in range(len(s)):
            currCost+=abs(ord(s[right])-ord(t[right]))

            while currCost>maxCost:
                currCost-=abs(ord(s[left])-ord(t[left]))
                left+=1

            maxLen=max(right-left+1,maxLen)

        return maxLen
