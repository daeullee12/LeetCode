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

        # if not root:
        #     return 0

        # q = deque([root])
        # level = 0
        
        # while q:
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)            
        
        #     level += 1

        # return level

        # Solution 3: Depth-First Search
        if not root:
            return 0

        s = [[root, 1]]
        res = 1

        while s:
            node, dep = s.pop()
            res = max(res, dep)
            if node.right:
                s.append([node.right, dep+1])
            if node.left:
                s.append([node.left, dep+1])
            
        return res


            




        

