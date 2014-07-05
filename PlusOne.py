class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        carry = 1
        length = len(digits)
        for i in range(length):
            tmp = digits[length - i - 1] + carry
            digits[length - i - 1] = tmp % 10
            if tmp < 10:
                return digits
            else:
                carry = tmp / 10
        if carry == 1:
            digits.insert(0,carry)
        return digits