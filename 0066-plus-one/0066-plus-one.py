class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # digits = digits[::-1]
        # carry, i = 1, 0
        # while carry:
        #     if i < len(digits):
        #         if digits[i] == 9:
        #             digits[i] = 0
        #         else: 
        #             digits[i] += 1
        #             carry = 0
            
        #     else:
        #         digits.append(1)
        #         carry = 0

        #     i += 1
        
        # return digits[::-1]

        carry = 1
        for i in range(len(digits)-1,-1,-1):         
            digits[i] += carry
            if digits[i] == 10:
                digits[i] = 0 
            else: carry = 0

            if i == 0 and carry:
                digits.insert(0, carry)
                carry = 0
            
        return digits