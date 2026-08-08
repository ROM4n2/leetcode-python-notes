# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev = None

        def reverse_preorder(node):
            if not node:
                return
            reverse_preorder(node.right)
            reverse_preorder(node.left)
            node.right = self.prev
            node.left = None
            self.prev = node
        
        reverse_preorder(root)
        
        
        '''if not root:
            return
        self.flatten(root.left)
        self.flatten(root.right)

        old_right = root.right

        root.right = root.left
        root.left = None

        p = root 
        while p.right:
            p = p.right
        p.right = old_right'''