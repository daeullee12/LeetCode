# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Solution 1: Recursive call, TC: O(n), SC: O(n)
        # if not root:
        #     return 0
                
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
        # without recursion, BFS & DFS available
        # Solution 2: Breadth-first search using Queue

        if not root:
            return 0
                
        q = deque([root])
        level = 0
        
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)            
        
            level += 1

        return level
            




        

