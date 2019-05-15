dynamic programing
subquestion: 有n个房子时，怎样抢到最多钱（好不文明
在n个房子面前，
 - 不抢，得到的最多的钱等于有n-1个房子时抢到的最多的钱
 - 抢，则第n-1个房子的钱肯定不能抢，得到的最多的钱=第n个房子的钱 + 第n-2个房子时能抢到的最多的钱，

比较两者的大小，决定抢不抢n

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) ==0 :
            return 0
        if len(nums) <= 2:
            return max(nums)
        max_incoming = [0]*len(nums)
        max_incoming[0] = nums[0]
        max_incoming[1] = max(nums[0], nums[1])
        for i in range(2,len(nums)):
            max_incoming[i] = max(max_incoming[i-1], max_incoming[i-2]+nums[i])
        return max(max_incoming)
```
