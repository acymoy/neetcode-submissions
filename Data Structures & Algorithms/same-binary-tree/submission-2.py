# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = []
        stack2 = []
        stack.append(p)
        stack2.append(q)
        while stack and stack2:
            n1 = stack.pop()
            n2 = stack2.pop()
            if n1 and n2:
                if n1.val != n2.val:
                    return False
                stack.append(n1.right)
                stack.append(n1.left)
                stack2.append(n2.right)
                stack2.append(n2.left)
            elif (n1 and not n2) or (n2 and not n1):
                return False
        return len(stack) == len(stack2)