class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = sub_res = nums[0]
        for i in range(1,len(nums)):
            sub_res = max(nums[i], nums[i] + sub_res)
            res = max(sub_res, res)
        return res
        

