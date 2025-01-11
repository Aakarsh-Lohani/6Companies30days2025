# https://leetcode.com/problems/excel-sheet-column-title/description/

# Time Complexity : O(logN)
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title=""
        while columnNumber>0:
            columnNumber-=1 # handling 1 based indexing
            rem=columnNumber%26
            title=chr(rem+65)+title
            columnNumber=columnNumber//26
        return title