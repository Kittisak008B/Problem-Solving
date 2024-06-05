# Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). 
# You may return the answer in any order.

# Example 1:
# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]

# Example 2:
# Input: words = ["cool","lock","cook"]
# Output: ["c","o"]

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        hm_1 = defaultdict(int)
        for char in words[0] :
            if char not in hm_1 :
                hm_1[char] = 0
            hm_1[char] += 1
        for word in words :
            hm_cur = defaultdict(int)
            for char in word :
                if char not in hm_cur :
                    hm_cur[char] = 0
                hm_cur[char] += 1
            for char in hm_1 :
                hm_1[char] = min(hm_1[char] , hm_cur[char])
        ans = []
        for char in hm_1 :
            for i in range(hm_1[char]) :
                ans.append(char)
        return ans 
        
# class Solution:
#     def commonChars(self, words: List[str]) -> List[str]:
#         hm = {}
#         for index , w in enumerate(words) :
#             for c in w :
#                 if c not in hm :
#                     hm[c] = [0]* len(words)
#                 hm[c][index] += 1
#         ans = []
#         for key in hm :
#             for i in range(min(hm[key])) :
#                 ans.append(key)
#         return ans
# Input: words = ["bella","label","roller"]
# hm = {'b': [1, 1, 0], 'e': [1, 1, 1], 'l': [2, 2, 2], 'a': [1, 1, 0], 'r': [0, 0, 2], 'o': [0, 0, 1]}
# Output: ["e","l","l"]
