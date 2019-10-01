class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def retp(root):
            if not root:
                return False
            l = retp(root.left)
            r = retp(root.right)
            if not l:
                root.left = None
            if not r:
                root.right = None
            return root.val == 1 or l or r
        return root if retp(root) else None