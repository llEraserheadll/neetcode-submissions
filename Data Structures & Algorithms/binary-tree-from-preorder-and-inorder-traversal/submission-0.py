# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hash_map = {val : idx for idx,val in enumerate(inorder)}
        idx_val = 0

        def dfs(l,r):
            nonlocal idx_val
            if l > r :
                return None
            
            root_val = preorder[idx_val]
            idx_val += 1

            root = TreeNode(root_val)
            mid = hash_map[root_val]
            root.left = dfs(l,mid - 1)
            root.right = dfs(mid + 1,r)
            return root


        
        return dfs(0,len(inorder) - 1)