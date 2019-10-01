class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def inorder(node):
            if node is not None:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)
        
        ans = cur = TreeNode(None)
        for v in inorder(root):
            print(v)
            cur.right = TreeNode(v)
            cur = cur.right
        return ans.right