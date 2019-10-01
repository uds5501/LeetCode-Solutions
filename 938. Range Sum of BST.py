# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.a = 0
        def inorder(root):
            if root:
                inorder(root.left)
                if root.val <= R and root.val >= L:
                    self.a += root.val
                inorder(root.right)
        inorder(root)
        return self.a
        