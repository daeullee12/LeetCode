class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        stack = []

        for s in tokens:
            if s in ["+", "-", "*", "/"]:
                a = stack.pop()
                b = stack.pop()
                if s == "+":
                    stack.append(a+b)
                elif s == "-":
                    stack.append(b-a)
                elif s == "*":
                    stack.append(a*b)
                else:
                    stack.append(int(float(b)/a))
            else:
                stack.append(int(s))
        
        return stack.pop()