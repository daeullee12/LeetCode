class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """



        # solution: stack, hashmap -> O(n), O(n)

        stack = []
        CloseToOpen = {")":"(", "]":"[", "}":"{"}
    
        for c in s:
            if c in CloseToOpen:
                if stack and stack[-1] == CloseToOpen[c]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False




            