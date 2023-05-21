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

        # Solution 1: recursive call, TC O(p+q)
        # if not p and not q:
        #     return True
    
        # if not p or not q or p.val != q.val:
        #     return False
        # return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        # Solution 2: BFS 
        
        # queue = deque([[p, q]])
     
        # while queue:
        #     node1, node2 = queue.popleft()
        #     if not node1 and not node2:
        #         continue
        #     elif not node1 or not node2 or node1.val != node2.val:
        #         return False
                
        #     queue.append([node1.left, node2.left])
        #     queue.append([node1.right, node2.right])
                    
        # return True


        # Solution 3: DFS

        stack = list([[p, q]])

        while stack:
            node1, node2 = stack.pop()
            if not node1 and not node2:
                continue
            elif not node1 or not node2 or node1.val != node2.val:
                return False
            stack.append([node1.right, node2.right])
            stack.append([node1.left, node2.left])
        return True
            
            




                



            