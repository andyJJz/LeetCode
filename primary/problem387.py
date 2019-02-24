#！/user/bin/env python
# _*_ coding;utf-8 _*_


class Solution:

    def firstUniqueChar(self,s):
        if len(s) < 1:
            return -1
        if len(s) == 1:
            return 0
        for i in range(len(s)):
            if s[i] not in s[i + 1:] and s[i] not in s[:i]:
                return i
        return -1




