# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

# Example 1:
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]

# Example 2:
# Input: s = "a"
# Output: [["a"]]

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        cur = []
        def is_palindrome(s) :
            i = 0
            j = len(s) - 1
            while i < j :
                if s[i] != s[j] :
                    return False
                i += 1
                j -= 1
            return True
        def backtrack(start) :
            if start == len(s) :
                ans.append(cur[:])
                return
            for end in range(start +1 , len(s)+1) :
                if is_palindrome(s[start:end]) :
                    cur.append(s[start:end])
                    backtrack(end)
                    cur.pop()
        backtrack(0)
        return ans
    #                       [   ]      
    #               /          |   \
    #            /             |     \
    #          /               |       \
    #     ['a']              ['aa']   ['aab']x 
    #     /      \             |
    #  ['a','a'] ['a','ab']x ['aa','b']           
    #    /
    #  ['a','a','b']       
