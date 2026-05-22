# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        first_node = ListNode()
        curr_node = first_node

        while list1 or list2:
            if list1 and list2: 
                if list1.val >= list2.val:
                    curr_node.next = list2
                    list2 = list2.next
                else:
                    curr_node.next = list1
                    list1 = list1.next
            else:
                if list1:
                    curr_node.next = list1
                    list1 = list1.next
                else:
                    curr_node.next = list2
                    list2 = list2.next
            curr_node = curr_node.next

        return first_node.next



        