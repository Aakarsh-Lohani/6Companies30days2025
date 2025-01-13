# https://leetcode.com/problems/sort-characters-by-frequency/description/

# Time Complexity : O(n) as sorting 26+26 elements takes constant time.
# Space Complexity : O(1) as 26+26 elements are stored
class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        res=""

        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1

        sorted_dict=dict(sorted(d.items(),key=lambda x:x[1], reverse=True))

        for j in sorted_dict:
            res+=j*sorted_dict[j]

        return res