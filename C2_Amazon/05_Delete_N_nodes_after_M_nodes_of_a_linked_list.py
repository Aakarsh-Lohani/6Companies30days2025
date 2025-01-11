# https://www.geeksforgeeks.org/problems/delete-n-nodes-after-m-nodes-of-a-linked-list/1


# Time Complexity: O(n) , n is no. of elements in the list
# Space Complexity : O(1) as constant extra space is required


# your task is to complete this Function
# Function shouldn't return anything

'''
class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def linkdelete(self, head, n, m):
        # Current node = head
        curr=head
        
        while curr: # Works until curr!=None
            
            # Skip m nodes
            for i in range(1,m):
                if curr is None:
                    return
                curr=curr.next
                
            if curr is None:
                return
            
            #Delete n nodes
            temp=curr.next
            for j in range(n):
                if temp is None:
                    break
                temp=temp.next
                
            # Join the current to temp
            curr.next=temp
            
            # Update curr for next cycle
            curr=curr.next  #curr=temp
