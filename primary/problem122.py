#！/user/bin/env python
# _*_ coding;utf-8 _*_


class Solution:

    def maxProfit(self,price):
        max = 0
        size = len(price)
        for i in range(size-1):
            if price[i]<price[i+1]:
                max += price[i+1] - price[i]
        return max





