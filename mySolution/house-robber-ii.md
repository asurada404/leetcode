[question](https://leetcode.com/problems/house-robber-ii/)
将问题 切分为1~n-1 和 2~n
代码还要再优化一下

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) < 4 : return max(nums)
        res = []
        for sub_nums in [nums[:-1], nums[1:]]:
            if len(sub_nums) ==0 :
                return 0
            if len(sub_nums) <= 2:
                return max(sub_nums)
            max_incoming = [0]*len(sub_nums)
            max_incoming[0] = sub_nums[0]
            max_incoming[1] = max(sub_nums[0], sub_nums[1])
            for i in range(2,len(sub_nums)):
                max_incoming[i] = max(max_incoming[i-1], max_incoming[i-2]+sub_nums[i])
            res.append(max_incoming[i])
        return max(res)

```
