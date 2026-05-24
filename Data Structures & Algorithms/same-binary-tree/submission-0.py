# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not q and not p:
            return True
        qq = deque()
        pq = deque()
        qq.append(q)
        pq.append(p)

        while qq or pq:
            q_node = qq.popleft()
            p_node = pq.popleft()
            if (q_node and not p_node) or (p_node and not q_node) or (q_node and p_node and q_node.val != p_node.val):
                return False
            if q_node:
                qq.append(q_node.left)
                qq.append(q_node.right)
            if p_node:
                pq.append(p_node.left)
                pq.append(p_node.right)

        return True

