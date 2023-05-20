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
        # solution 1: TC O(n^2)
        # if not root: return True

        # height_diff = abs(self.depth(root.left) - self.depth(root.right))

        # if height_diff <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
        #     return True

        # return False

        # solution 2: TC O(n)

        def dfs(root):
            if not root: return [True, 0]
            left, right = dfs(root.left), dfs(root.right)
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]

