# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        first_node = ListNode()
        curr_node = first_node
        curr_one = list1
        curr_two = list2

        while curr_one or curr_two:
            if not curr_one or not curr_two: 
                if curr_one and not curr_two:
                    curr_node.next = curr_one
                    curr_one = curr_one.next
                elif curr_two and not curr_one:
                    curr_node.next = curr_two
                    curr_two = curr_two.next
            else:
                if curr_one.val >= curr_two.val:
                    curr_node.next = curr_two
                    curr_two = curr_two.next
                else:
                    curr_node.next = curr_one
                    curr_one = curr_one.next
            curr_node = curr_node.next

        return first_node.next



        