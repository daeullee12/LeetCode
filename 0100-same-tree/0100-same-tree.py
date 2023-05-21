# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        iter1 = p
        iter2 = q

        if not iter1 and not iter2:
            return True
    
        elif (iter1 and not iter2) or (not iter1 and iter2):
            return False
        else:
            return iter1.val == iter2.val and self.isSameTree(iter1.left, iter2.left) and self.isSameTree(iter1.right, iter2.right)


                



            