#！/user/bin/env python
# _*_ coding;utf-8 _*_


class Solution:

    def moveZeros(self,nums):
        length = len(nums)
        if length <= 1:
            return
        zero_count = 0
        i = 0
        while i < length:
            if nums[i] == 0:
                zero_count += 1
            else:
                nums[i - zero_count] = nums[i]
            i += 1

        j = 1
        while j <= zero_count:
            nums[length - j] = 0
            j += 1

