# You are given two string arrays words1 and words2.
# A string b is a subset of string a if every letter in b occurs in a including multiplicity.
# For example, "wrr" is a subset of "warrior" but is not a subset of "world".
# A string a from words1 is universal if for every string b in words2, b is a subset of a.
# Return an array of all the universal strings in words1. You may return the answer in any order.

# Example 1:
# Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
# Output: ["facebook","google","leetcode"]

# Example 2:
# Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]
# Output: ["apple","google","leetcode"]
 
# Constraints:
# 1 <= words1.length, words2.length <= 10**4
# 1 <= words1[i].length, words2[i].length <= 10
# words1[i] and words2[i] consist only of lowercase English letters. All the strings of words1 are unique.

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        d = defaultdict(int)
        res = []
        for w in words2 :
            c2 = defaultdict(int)
            for char in w :
                c2[char] += 1
            for char in c2 :
                d[char] = max(d[char] , c2[char])
        for w in words1 :
            c1 = defaultdict(int)
            for char in w :
                c1[char] += 1
            success = True
            for char in d :
                if c1[char] < d[char] :
                    success = False
                    break
            if success :
                res.append(w)
        return res
'''
words1 = ["cat" , "bat" , "subject"]
words2 = ["ct" , "bt"]

"ct" c2 = {"c":1 ,"t":1}
"bt" c2 = {"b":1 ,"t":1}
d = {"c":1 ,"t":1 ,"b":1}

"cat"     c1 = {"c":1 , "a":1 , "t":1}  fail dont have 'b'
"bat"     c1 = {"b":1 , "a":1 , "t":1}  fail dont have 'c'
"subject" c1 = {"s":1,"u":1,"b":1,"j":1,"e":1,"c":1,"t":1}  success (have 1'c' 1't' 1'b' in word)
'''
