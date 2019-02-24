#！/user/bin/env python
# _*_ coding;utf-8 _*_


class Solution:

    def reverseString(self,s):
        size = int(len(s)/2)
        for i in range(size):
            temp = s[i]
            s[i] = s[len(s)-i-1]
            s[len(s)-i-1] = temp
        return s

