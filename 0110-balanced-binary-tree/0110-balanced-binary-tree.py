# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        height_diff = abs(self.depth(root.left) - self.depth(root.right))

        if height_diff <= 1 and (self.isBalanced(root.left) and self.isBalanced(root.right)):
            return True

        return False
    
    def depth(self, root):
        if not root:
            return 0
        return 1 + max(self.depth(root.left), self.depth(root.right))