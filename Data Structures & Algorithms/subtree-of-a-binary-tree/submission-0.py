# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    def isSameTree(self, q, p):
        if not q and not p:
            return True

        qq = deque([q])
        pq = deque([p])

        while pq:
            q_node = qq.popleft()
            p_node = pq.popleft()
            if not q_node and not p_node:
                continue
            if (not q_node and p_node) or (not p_node and q_node) or (q_node.val != p_node.val):
                return False
            qq.append(q_node.left)
            qq.append(q_node.right)
            pq.append(p_node.left)
            pq.append(p_node.right)

        return True

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # iterate through all the nodes in root
        if not root and not subRoot:
            return True

        q = deque([root])
        while q:
            q_node = q.popleft()
            if self.isSameTree(q_node, subRoot):
                return True
            if q_node:
                q.append(q_node.left)
                q.append(q_node.right)
        return False