# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs_preorder(node, res):
            if not node:
                return None
            res.append(node.val)
            dfs_preorder(node.left, res)
            dfs_preorder(node.right, res)
        dfs_preorder(root, res)
        return res