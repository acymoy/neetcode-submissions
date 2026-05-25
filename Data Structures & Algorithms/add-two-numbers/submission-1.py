# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def add(self, n1, n2, carry): 
        if not n1 and not n2 and not carry:
            return None

        val1 = n1.val if n1 else 0
        val2 = n2.val if n2 else 0

        s = (val1 + val2 + carry) % 10
        carry = (val1 + val2 + carry) // 10

        n1_next = n1.next if n1 else None
        n2_next = n2.next if n2 else None

        return ListNode(s, self.add(n1_next, n2_next, carry))

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
       return self.add(l1, l2, 0)

