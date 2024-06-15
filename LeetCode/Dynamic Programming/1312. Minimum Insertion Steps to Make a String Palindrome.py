# Given a string s. In one step you can insert any character at any index of the string.
# Return the minimum number of steps to make s palindrome.
# A Palindrome String is one that reads the same backward as well as forward.

# Example 1:
# Input: s = "zzazz"
# Output: 0
# Explanation: The string "zzazz" is already palindrome we do not need any insertions.

# Example 2:
# Input: s = "mbadm"
# Output: 2
# Explanation: String can be "mbdadbm" or "mdbabdm".

# Example 3:
# Input: s = "leetcode"
# Output: 5
# Explanation: Inserting 5 characters the string becomes "leetcodocteel".

class Solution:
    def minInsertions(self, s: str) -> int:
        dp = {}
        def dfs(i , j) :
            if i >= j :
                return 0
            if (i , j) in dp :
                return dp[(i , j)]
            if s[i] == s[j] :
                dp[(i , j)] = dfs(i + 1 , j - 1)
                return dp[(i , j)]
            else :
                dp[(i , j)] = min(1 + dfs(i + 1 , j) , 1 + dfs(i , j - 1) ) #insert on right or left
                return dp[(i , j)]       
        return dfs(0 , len(s) - 1)
'''
bad   badb  bdadb
i j    ij     i
              j
                  bad
                  i j
                /     \
            badb      dbad       step=1
             ij        ij 
            / \        /  \ 
        badab bdadb dbabd dabad  step=2 
          i     i     i     i 
          j     j     j     j
