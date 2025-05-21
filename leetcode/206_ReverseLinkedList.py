# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return head
        
        move_node=head
        prev_node = None

        while move_node:
            curr_node = move_node
            move_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node

        return curr_node
