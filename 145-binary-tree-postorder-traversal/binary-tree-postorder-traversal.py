class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs_postorder(node, res):
            if not node:
                return None
            dfs_postorder(node.left, res)
            dfs_postorder(node.right, res)
            res.append(node.val)
        dfs_postorder(root, res)
        return res