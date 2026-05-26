# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def searchTree(self, root, target):
        if root.val == target:
            return True

        left_find, right_find = False, False
        if root.left:
            left_find = self.searchTree(root.left, target)
        if root.right:
            right_find = self.searchTree(root.right, target)
        
        return left_find or right_find

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        is_ancestor = self.searchTree(root, p.val) and self.searchTree(root, q.val)

        left_is_ancestor, right_is_ancestor = None, None
        if root.left:
            left_is_ancestor = self.lowestCommonAncestor(root.left, p, q)
        if root.right:
            right_is_ancestor = self.lowestCommonAncestor(root.right, p, q)

        if is_ancestor and (not left_is_ancestor and not right_is_ancestor):
            return root

        return left_is_ancestor or right_is_ancestor