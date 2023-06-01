class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = digits[::-1]
        carry, i = 1, 0
        while carry:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else: 
                    digits[i] += 1
                    carry = 0
            
            else:
                digits.append(1)
                carry = 0

            i += 1
        
        return digits[::-1]