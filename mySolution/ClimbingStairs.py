class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        a = 1
        b = 2
        for i in range(2,n):
            b, a = b + a,  b
        return b
            
        

        `
