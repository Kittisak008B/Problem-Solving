# Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

# Example 1:
# Input: n = 13
# Output: 6

# Example 2:
# Input: n = 0
# Output: 0
 
# Constraints:  0 <= n <= 10**9

class Solution:
    def countDigitOne(self, n: int) -> int:
        ans = 0 
        base = 1
        while base <= n :
            left = (n // base) // 10
            cur = (n // base) % 10
            right = n % base
            if cur == 1 :
                ans += left*base + right + 1
            elif cur > 1 :
                ans += (left+1)*base
            elif cur < 1 :
                ans += left*base
            base *= 10
        return ans      
'''
13 :  No. of 1 at one's place= 2 -> 1 11
             1 at ten's palce= 4 -> 10 11 12 13
             total No. of digit one = 2 + 4 = 6

21 : No. of 1 at one's place= 3 -> 1 11 21
            1 at ten's place= 10 -> 10 11 12 13 14 15 16 17 18 19

n = 112
left cur right base
11    2    0     1    ans+=12   -> 1 11 21 31 41...101 111    
 1    1    2    10    ans+=13   -> 10 11 12...19 110 111 112  
 0    1   12   100    ans+=13   -> 100 101...112

 if cur==1 : ans+= left*base+right+1
    cur>1  : ans+= (left+1)*base
    cur<1  : ans+= left*base
'''
