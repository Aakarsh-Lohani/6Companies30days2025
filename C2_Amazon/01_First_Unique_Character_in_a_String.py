# https://leetcode.com/problems/first-unique-character-in-a-string/description/4

# Time Complexity: O(n) single pass
# Space Complexity: O(n) due to storage of all indices in worst case
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={}
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]].append(i)
            else:
                d[s[i]]=[i]

        for a in d:
            if len(d[a])==1:
                res=d[a][0]
                return res
        return -1

# Time Complexity : O(n) double pass
# Space Complexity: O(1) as only 26 alplhabets are stored in worst case
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for i in s:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        
        for j in range(len(s)):
            if count[s[j]]==1:
                return j

        return -1
