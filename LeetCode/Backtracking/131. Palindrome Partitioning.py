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

        def bt(start) :
            if start == len(s) :
                ans.append(cur[:])
                return
            for i in range(start+1 , len(s)+1) :
                if is_palindrome(s[start:i]) :
                    cur.append(s[start:i])
                    bt(i)
                    cur.pop()
        bt(0)
        return ans
    '''
    s ='aab' len(s) = 3

    bt(0) start = 0  i = 1 cur =[a] bt(1) 
    bt(1) start = 1  i = 2 cur =[a,a] bt(2)
    bt(2) start = 2  i = 3 cur =[a,a,b] bt(3)
    bt(3) start = 3 =len(s) --> ans = [[a,a,b]] return
    bt(1) start = 1  i = 3 cur =[a,ab] x
    bt(0) start = 0  i = 2 cur =[aa] bt(2)
    bt(2) start = 2  i = 3 cur =[aa,b] bt(3)
    bt(3) start = 3 =len(s) --> ans = [[a,a,b] , [aa,b]] return
    bt(0) start = 0  i = 3 cur =[aab] x
    '''
    #                _____ [  ] ___     
    #               /          |   \
    #            /             |     \
    #          /               |       \
    #     ['a']              ['aa']   ['aab']x  start=0
    #     /      \             |
    #  ['a','a'] ['a','ab']x   |                start=1
    #    /                     |
    #  ['a','a','b']        ['aa','b']          start=2    
    
