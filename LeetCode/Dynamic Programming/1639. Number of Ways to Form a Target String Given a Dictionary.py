# You are given a list of strings of the same length words and a string target. Your task is to form target using the given words under the following rules:
# target should be formed from left to right.
# To form the ith character (0-indexed) of target, you can choose the kth character of the jth string in words if target[i] = words[j][k].
# Once you use the kth character of the jth string of words, you can no longer use the xth character of any string in words where x <= k. 
# In other words, all characters to the left of or at index k become unusuable for every string.
# Repeat the process until you form the string target.
# Notice that you can use multiple characters from the same string in words provided the conditions above are met.
# Return the number of ways to form target from words. Since the answer may be too large, return it modulo 109 + 7.

# Example 1:
# Input: words = ["acca","bbbb","caca"], target = "aba"
# Output: 6
# Explanation: There are 6 ways to form target.
# "aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("caca")
# "aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("caca")
# "aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("acca")
# "aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("acca")
# "aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("acca")
# "aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("caca")

# Constraints: 1 <= words.length <= 1000     1 <= words[i].length <= 1000     All strings in words have the same length.    
#              1 <= target.length <= 1000    words[i] and target contain only lowercase English letters.

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        mod = 1_000_000_007
        col = []
        for x in zip(*words) :
            #print(x)
            s = defaultdict(int)
            for char in x :
                s[char] += 1
            col.append(s)
        #print(col)
        dp = {}
        def dfs(i , j) :
            if i >= len(target) : #cover the target
                return 1
            if j >= len(words[0]) : #cover each word
                return 0
            if (i , j) in dp :
                return dp[(i , j)]
            res = dfs(i , j+1) #skip jth index 
            if col[j][target[i]] != 0 : #if char in col[j]
                res += dfs(i+1 , j+1) * col[j][target[i]] #pick jth index
            dp[(i , j)] = res % mod
            return dp[(i , j)]
        return dfs(0 , 0)
'''
words = ["acca","bbbb","caca"], target = "aba"

('a', 'b', 'c')
('c', 'b', 'a')
('c', 'b', 'c')
('a', 'b', 'a')

col = [defaultdict(<class 'int'>, {'a': 1, 'b': 1, 'c': 1}), 
       defaultdict(<class 'int'>, {'c': 1, 'b': 1, 'a': 1}), 
       defaultdict(<class 'int'>, {'c': 2, 'b': 1}), 
       defaultdict(<class 'int'>, {'a': 2, 'b': 1}) ]

'''
