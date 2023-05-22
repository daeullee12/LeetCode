# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0
        if not root.left or not root.right:
            return self.depth(root) - 1
        
        diameter = self.depth(root.left) + self.depth(root.right) 
        max_diameter_before = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        
        return max(diameter, max_diameter_before)

    def depth(self, root):
        if not root:
            return 0
        return 1 + max(self.depth(root.left), self.depth(root.right))
        
        # 왼쪽 자식 깊이 + 오른쪽 자식 깊이 + 2 or 왼쪽 diameter or 오른쪽 diameter
    


        
