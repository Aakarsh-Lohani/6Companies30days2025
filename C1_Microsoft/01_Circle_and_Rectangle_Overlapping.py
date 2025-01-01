# https://leetcode.com/problems/circle-and-rectangle-overlapping/description/

# Time Complexity : O(1) as no. of operations don't depend on size of input.
# Space Complexity : O(1) as there is no need of extra space relative to size of input. 
class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:

        #Find the closest point on rect to the circle
        x=max(x1,min(xCenter,x2))
        y=max(y1,min(yCenter,y2))

        #Min Distance between the point(x,y) and circle
        x1=x-xCenter
        y1=y-yCenter

        #Checking if it lies inside the circle
        if (x1*x1)+(y1*y1)<=radius*radius:
            return True
        return False

