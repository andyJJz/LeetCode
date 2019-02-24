#！/user/bin/env python
# _*_ coding;utf-8 _*_


class Solution:

    def removeDuplicates(self,nums):
        if not nums:
            return 0
        len_list = len(nums)
        i = 0
        for j in range(1,len_list):
            if nums[i] != nums[j]:
                nums[i+1] = nums[j]
                i += 1
        return i+1



