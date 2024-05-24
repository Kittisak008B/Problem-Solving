# Given a list of words, list of  single letters (might be repeating) and score of every character.
# Return the maximum score of any valid set of words formed by using the given letters (words[i] cannot be used two or more times).
# It is not necessary to use all characters in letters and each letter can only be used once. Score of letters 'a', 'b', 'c', ... ,'z' is given by score[0], score[1], ... , score[25] respectively.

# Example 1:
# Input: words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
# Output: 23
# Explanation:
# Score  a=1, c=9, d=5, g=3, o=2
# Given letters, we can form the words "dad" (5+1+5) and "good" (3+2+2+5) with a score of 23.
# Words "dad" and "dog" only get a score of 21.

# Example 3:
# Input: words = ["leetcode"], letters = ["l","e","t","c","o","d"], score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
# Output: 0
# Explanation:
# Letter "e" can only be used once.

# Constraints:   words[i], letters[i] contains only lower case English letters.

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:

        def get_score(word) :
            res = 0
            for c in word :
                res += score[ord(c) - ord('a')]
            return res 

        def check_can_make_word(word , letter_cnt) :
            word_cnt = defaultdict(int)
            for c in word :
                if c not in word_cnt :
                    word_cnt[c] = 0
                word_cnt[c] += 1

            for c in word_cnt :
                if word_cnt[c] > letter_cnt[c] :
                    return False
            return True
        
        letter_cnt = defaultdict(int)
        for c in letters :
            if c not in letter_cnt :
                letter_cnt[c] = 0
            letter_cnt[c] += 1

        def bt(i) :
            if i == len(words) :
                return 0
            ans = bt(i+1)
            if check_can_make_word(words[i] , letter_cnt) :
                for c in words[i] :
                    letter_cnt[c] -= 1
                ans = max(ans , get_score(words[i]) + bt(i+1) )
                for c in words[i] :
                    letter_cnt[c] += 1
            return ans
        return bt(0)
      


