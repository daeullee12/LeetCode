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

    #     if not root:
    #         return 0
    #     if not root.left or not root.right:
    #         return self.depth(root) - 1
        
    #     diameter = self.depth(root.left) + self.depth(root.right) 
    #     max_diameter_before = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        
    #     return max(diameter, max_diameter_before)

    # def depth(self, root):
    #     if not root:
    #         return [0, 0]
    #         left, right =
    #     return 1 + max(self.depth(root.left), self.depth(root.right))
        
        def dfs(root):
            if not root: return [0, 0] #[diameter, height]
            if not root.left and not root.right: return [0, 0]
            
            left, right = dfs(root.left), dfs(root.right)
            if not root.left or not root.right:
                diameter = 1 + left[1] + right[1]
            else: 
                diameter = max(left[0], right[0], 2 + left[1] + right[1])

            return [diameter, 1 + max(left[1], right[1])]


        return dfs(root)[0]    


        
