class Solution:
    def countAndSay(self, n: int) -> str:
        ### leetcode 1
        s = '1'
        res = s

        for i in range(n-1):
            count = 1
            s = s + '#'
            res = ''
            for i in range(len(s)-1):
                if s[i] == s[i+1]:
                    count = count +1
                else:
                    res = res + str(count) + s[i]
                    count = 1
            s = res
        return res
        
    
        
