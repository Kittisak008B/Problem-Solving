# Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. 
# Return all such possible sentences in any order.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.

# Example 1:
# Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
# Output: ["cats and dog","cat sand dog"]

# Example 2:
# Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
# Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
# Explanation: Note that you are allowed to reuse a dictionary word.

# Example 3:
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: []
 
# Constraints:   s and wordDict[i] consist of only lowercase English letters.   All the strings of wordDict are unique.   Input is generated in a way that the length of the answer doesn't exceed 105.
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        cur = []
        set_wordDict = set(wordDict)
        def bt(start) :
            if start == len(s) :
                ans.append(' '.join(cur[:]))
                return 
            for i in range(start , len(s)) :
                word = s[start : i+1] 
                if word in set_wordDict :
                    cur.append(word)
                    bt(i+1)
                    cur.pop()
        bt(0)
        return ans
      
