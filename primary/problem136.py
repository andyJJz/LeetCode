#！/user/bin/env python
# _*_ coding;utf-8 _*_


class Solution:

    def singleNumber(self,nums):
        i = 0
        for j in nums:
            i ^= j
        return i

