#！/user/bin/env python
# _*_ coding;utf-8 _*_


class Solution:

    def containsDuplicate(self,nums):
        sorted_nums = sorted(nums)
        for i in range(1,len(nums)):
            if sorted_nums[i-1] == sorted_nums[i]:
                return True
        return False


