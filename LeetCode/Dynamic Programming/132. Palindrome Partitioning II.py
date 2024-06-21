# Given a string s, partition s such that every substring of the partition is a palindrome.
# Return the minimum cuts needed for a palindrome partitioning of s.

# Example 1:
# Input: s = "aab"
# Output: 1
# Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
  
# Example 2:
# Input: s = "a"
# Output: 0

# Example 3:
# Input: s = "ab"
# Output: 1
 
# Constraints:  1 <= s.length <= 2000    s consists of lowercase English letters only.

class Solution:
    def minCut(self, s: str) -> int:
        d = defaultdict(set)
        def palindrome_from_mid(left, right) :
            while left >= 0 and right < len(s) and s[left] == s[right] :
                #d[(left,right)].add(s[left:right+1])   ### Memory Limit Exceeded
                d[(left,right)].add('Palindrome')
                left -= 1
                right += 1
        for i in range(len(s)) :
            palindrome_from_mid(i,i)     #check odd length  ex. a  aaa
            palindrome_from_mid(i,i+1)   #check even length ex. aa  aaaa
        # print(d)
        dp = {}
        def dfs(left , right) :
            if (left , right) in d : # if this already palindrome don't need to cut it 
                return 0
            if (left , right) in dp :
                return dp[(left , right)]
            cut = len(s)
            for i in range(left , right) : 
                if (left , i) in d : 
                    cut = min(cut , 1 + dfs(i + 1 , right))
            dp[(left , right)] = cut
            return dp[(left , right)]
        return dfs(0 , len(s)-1)
'''
s = "aab"
     l r
 idx 0 2  ->i=0,1 (0,0) 'a' in d->cut= 1+dfs(1,2)  ('ab'  i=1 (1,1) 'a' in d -> cut 1+dfs(2,2) ('b' left b is palindrome no cut))
                                    -> 1+1+0 = 2 
                  (0,1)'aa' in d->cut= 1+dfs(2,2)  ('b' left b is palindrome no cut)-> 1+0=1 #min

                 aab
                /   \
            a|ab    aa|b
            /          \
           a|b          b  this path 1 cut  ##min cuts     Time: O(n**2) Space: O(n**2)
           /
          b -> already palindrome don't need to cut  
          this path 2 cuts                              
'''
