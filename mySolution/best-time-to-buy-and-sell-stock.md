dynamic programing

子问题：第i天卖出的话哪一天买入比较合适

``` python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profile = 0
        if len(prices) == 0:
            return 0
        min_price = prices[0]
        for i in range(1,len(prices)):
            min_price = min(min_price, prices[i] ) ## 最小价格是第i天的价格还是最前的最小价格
            max_profile = max(max_profile, prices[i]-min_price)  ##第i天卖出的获利更大还是之前（子问题）的获利更大
        return max_profile
        
```
