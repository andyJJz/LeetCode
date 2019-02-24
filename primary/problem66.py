#！/user/bin/env python
# _*_ coding;utf-8 _*_


class Solution:

    def plusOne(self,digits):
        size = len(digits)
        sum = 0
        for i in range(size):
            sum += digits[i] * (10**(size-i-1))
        plus = sum + 1
        plus_str = str(plus)
        plus_size = len(plus_str)
        result = []
        for i in range(plus_size):
            a = int(plus_str[i])
            result.append(a)
        return result


