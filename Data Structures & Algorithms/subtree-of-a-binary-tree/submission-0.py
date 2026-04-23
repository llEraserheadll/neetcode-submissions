# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.issameTree(root,subRoot):
            return True
        return (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot))
        


    def issameTree(self,p,q):
        if not p and not q:
            return True
        
        if p and q and p.val == q.val:
            return self.issameTree(p.left,q.left) and self.issameTree(p.right,q.right)
        else:
            return False