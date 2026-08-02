# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        if(slow == None):
            return False
        fast = slow.next
        while (slow != fast and fast != None):
            slow = slow.next
            if(fast.next == None):
                return False
            else:
                fast = fast.next.next
        
        if(fast == None):
            return False
        else:
            return True