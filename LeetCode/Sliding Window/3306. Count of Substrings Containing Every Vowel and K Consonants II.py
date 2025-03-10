# You are given a string word and a non-negative integer k.
# Return the total number of substrings of word that contain every vowel ('a', 'e', 'i', 'o', and 'u') at least once and exactly k consonants.

# Example 1:
# Input: word = "aeioqq", k = 1
# Output: 0
# Explanation:
# There is no substring with every vowel.

# Example 2:
# Input: word = "aeiou", k = 0
# Output: 1
# Explanation:
# The only substring with every vowel and zero consonants is word[0..4], which is "aeiou".

# Example 3:
# Input: word = "ieaouqqieaouqq", k = 1
# Output: 3
# Explanation:
# The substrings with every vowel and one consonant are:
# word[0..5], which is "ieaouq".
# word[6..11], which is "qieaou".
# word[7..12], which is "ieaouq".
 
# Constraints:
# 5 <= word.length <= 2 * 10**5
# word consists only of lowercase English letters.
# 0 <= k <= word.length - 5

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def atLeastK_consonants(k) :
            vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
            has_vowels = set()
            l = 0
            res = 0
            consonants = 0
            n = len(word)
            for r in range(n) :
                if word[r] in vowels :
                    vowels[word[r]] += 1
                    has_vowels.add(word[r])
                else:
                    consonants += 1
                while len(vowels) == len(has_vowels) and consonants >= k :
                    res += n - r
                    if word[l] in vowels :
                        vowels[word[l]] -= 1
                        if vowels[word[l]] == 0 :
                            has_vowels.remove(word[l])
                    else:
                        consonants -= 1
                    l += 1
            return res
        return atLeastK_consonants(k) - atLeastK_consonants(k + 1)
'''
"aeiouxxa" k=1   
        at least 1 consonants -> 4 : aeioux , aeiouxx , aeiouxxa , eiouxxa
        at least 2 consonants -> 3 : aeiouxx , aeiouxxa , eiouxxa
        exactly 1 consonants = at least 1 consonants - at least 2 consonants = 4 - 3 = 1 -> aeioux
'''
