# https://leetcode.com/problems/find-the-winner-of-the-circular-game/description/


# Optimized approach using Josephus Problem Formula

# The position of the last remaining person can be determined using the formula: [ J(n, k) = (J(n-1, k) + k) % n ] where (J(1, k)=0). 
# Converting it to iterative approach ,the position of the last remaining person can be found by considering the position of the last remaining person among ( n-1 ) people and adjusting it for the current circle size ( n )

# Time Complexity :O(n)
# Space Complexity :O(1)
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        winner=0  
        for i in range(2,n+1):
            winner=(winner+k)%i
        return winner+1





# Brute force

# Time Complexity: O(n*k) - The while loop runs n-1 times and each deletion takes O(n) in the worst case.
# Space Complexity: O(n) - The list `friends` stores n elements initially.
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends=list(range(1,n+1))
        idx=0

        while len(friends)>1:
            idx=(idx+k-1)%len(friends)
            del friends[idx]

        return friends[0]