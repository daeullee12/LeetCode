class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        stack = []

        for s in tokens:
            if s == "+":
                stack.append(stack.pop() + stack.pop())
            elif s == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif s == "*":
                stack.append(stack.pop() * stack.pop())
            elif s == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(s))
        
        return stack.pop()