# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes = []

        def getNodes(node):
            if not node or len(nodes) >= k:
                return
            getNodes(node.left)
            nodes.append(node.val)
            getNodes(node.right)

            return

        getNodes(root)

        print(nodes)

        return nodes[k - 1]

