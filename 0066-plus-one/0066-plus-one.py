class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = str()
        for n in digits:
            s += str(n)
        
        output = int(s) + 1
        l = []
        print(output)
        while output:
            l.insert(0,output % 10)
            output //= 10
        
        return l