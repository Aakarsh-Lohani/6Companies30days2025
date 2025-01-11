# https://leetcode.com/problems/friends-of-appropriate-ages/description/

# Other approaches : binary search and two pointers 
# 1. Using dictionary to count the unique ages
# Time Complexity: O(n) as , O(k^2+n), 0<=k<=120 , so O(n)
# Space Complexity : O(1) , 121 unique ages at max
from typing import List
from collections import Counter
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        count=Counter(ages)
        total=0

        # For each unique age check if holds the conditions
        for i in count:
            for j in count:
                if j<= (0.5)*i+7 or j>i or (j >100 and i<100):
                    continue
                else:
                    # Dont send request to itself
                    if i==j:
                        total+=count[i]*(count[i]-1)
                    else:
                        # Count all possible requests
                        total+=count[i]*count[j]
        return total
