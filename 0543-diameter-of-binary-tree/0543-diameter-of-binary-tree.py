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
        max_dia = [0] 

        def dfs(root):
            if not root: return -1          
            left, right = dfs(root.left), dfs(root.right)
            max_dia[0] = max(max_dia[0], 2 + left + right)
            return 1 + max(left, right)

        dfs(root)

        return max_dia[0] 


        
