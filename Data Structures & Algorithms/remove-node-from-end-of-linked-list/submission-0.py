# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list_length = 0
        c = head
        while c:
            list_length += 1
            c = c.next

        res = ListNode()
        res.next = head
        beginning_node = res
        
        node_to_remove = list_length - n # index to remove, starting from 0
        i = -1
        while i <= node_to_remove:
            if i == node_to_remove - 1: # if at the node before the one we need to skip
                print('reached node')
                res.next = res.next.next
                return beginning_node.next
            i += 1
            res = res.next


        return beginning_node.next