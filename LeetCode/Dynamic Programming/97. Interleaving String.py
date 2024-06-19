# Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
# An interleaving of two strings s and t is a configuration where s and t are divided into n and m substrings respectively, such that:
# s = s1 + s2 + ... + sn
# t = t1 + t2 + ... + tm
# |n - m| <= 1
# The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
# Note: a + b is the concatenation of strings a and b.

# Example 1:
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
# Explanation: One way to obtain s3 is:
# Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
# Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
# Since s3 can be obtained by interleaving s1 and s2, we return true.

# Example 2:
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false
# Explanation: Notice how it is impossible to interleave s2 with any other string to obtain s3.

# Example 3:
# Input: s1 = "", s2 = "", s3 = ""
# Output: true
 
# Constraints:  s1, s2, and s3 consist of lowercase English letters.

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}
        def dfs(i , j , k) :
            if i >= len(s1) and j >= len(s2) and k >= len(s3) :
                return True
            if (i , j , k) in dp :
                return dp[(i , j , k)]
            if i < len(s1) and s1[i] == s3[k] and dfs(i+1 , j , k+1) :
                dp[(i , j , k)] = True
                return dp[(i , j , k)]
            if j < len(s2) and s2[j] == s3[k] and dfs(i , j+1 , k+1) :
                dp[(i , j , k)] = True
                return dp[(i , j , k)]
            dp[(i , j , k)] = False
            return dp[(i , j , k)]
            
        if len(s1) + len(s2) != len(s3) :
            return False
        return dfs(0 , 0 , 0)
'''
s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
      i             j             k

                (i,j,k)
         _______(0,0,0)_______
        /s1[i]==s3[k]         \s2[j]==s3[k]
     (i+1=1,j=0,k+1=1)
     /        \ 
  (2,0,2)
  /      \
       (2,1,3)____
        /         \
  (3,1,4)         (2,2,4)__   
  /    \            /      \ 
    (3,2,5)     (3,2,5)    (2,3,5)
      /   \      in dp       /   \
  (4,2,6)                        (2,4,6)
  /    \                          /   \ 
      (4,3,7)                  (3,4,7)  
      /     \                    /    \
  (5,3,8)x  (4,4,8)            (4,4,8)
            /    \              in dp
                 (4,5,9)
                  /    \ 
             (5,5,10)  
               True 
'''
# class Solution:
#     def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
#         dp = {}
#         def dfs(i , j , k) :
#             if i >= len(s1) and j >= len(s2) and k >= len(s3) :
#                 return True
#             if (i , j , k) in dp :
#                 return dp[(i , j , k)]
#             dp[(i , j , k)] = ( (i<len(s1) and s1[i]==s3[k] and dfs(i+1,j,k+1)) or 
#                                 (j<len(s2) and s2[j]==s3[k] and dfs(i,j+1,k+1)) ) and k<len(s3)
#             return dp[(i , j , k)]      
#         if len(s1) + len(s2) != len(s3) :
#             return False
#         return dfs(0 , 0 , 0)
