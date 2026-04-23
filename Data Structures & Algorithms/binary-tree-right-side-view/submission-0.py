# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        q.append(root)
        view = []

        while q:
            qlen = len(q)
            rightnode = None

            for i in range(qlen):
                node = q.popleft()
                if node:
                    rightnode = node
                    q.append(node.left)
                    q.append(node.right)

            if rightnode:
                view.append(rightnode.val)
        
        return view

        