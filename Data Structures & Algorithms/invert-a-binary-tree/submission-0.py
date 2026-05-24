# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rec(self, root: TreeNode):
        if not root.left and not root.right:
            return root

        left = root.left
        right = root.right

        if left:
            left = self.rec(left)
        if right:
            right = self.rec(right)

        root.left = right
        root.right = left

        return root

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        return self.rec(root)