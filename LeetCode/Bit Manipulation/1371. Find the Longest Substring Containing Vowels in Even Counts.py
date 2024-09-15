# Given the string s, return the size of the longest substring containing each vowel an even number of times. 
# That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.

# Example 1:
# Input: s = "eleetminicoworoep"
# Output: 13
# Explanation: The longest substring is "leetminicowor" which contains two each of the vowels: e, i and o and zero of the vowels: a and u.

# Example 2:
# Input: s = "leetcodeisgreat"
# Output: 5
# Explanation: The longest substring is "leetc" which contains two e's.

# Example 3:
# Input: s = "bcbcbc"
# Output: 6
# Explanation: In this case, the given string "bcbcbc" is the longest because all vowels: a, e, i, o and u appear zero times.
 
# Constraints:  1 <= s.length <= 5 x 10^5    s contains only lowercase English letters.

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {'a': 1,     # 00001 in binary
                  'e': 2,     # 00010 
                  'i': 4,     # 00100 
                  'o': 8,     # 01000 
                  'u': 16,    # 10000 
                 }
        d = {0: -1}
        state , res = 0 , 0
        for i , c in enumerate(s) :
            if c in vowels :
                state ^= vowels[c]
            if state in d :
                res = max(res, i - d[state])
            else :
                d[state] = i
        return res
'''
eleetminicoworoep      'e' → 00010   state = 0 ^ 2 = 2    
↑                       d = {0:-1 , 2:0}

eleetminicoworoep      'l' is not a vowel, so the state doesn't change. res = 1
 ↑                      

eleetminicoworoep       state = 2 ^ 2 = 0
  ↑                     seen state 0 before at index -1   res = 2 - (-1) = 3 (substring "ele")
                       
eleetminicoworoep       state = 0 ^ 2 = 2
   ↑                    seen this state  before, at index 0 , res = 3 - 0 = 3
                        
eleetminicoworoep       state doesn't change, res = 4-d[2] = 4 (substring "leet")
    ↑                   

eleetminicoworoep       state doesn't change, res = 5 (substring "leetm")
     ↑           

eleetminicoworoep       state = 2 ^ 4 = 00110 = 6
      ↑                 haven't seen this state before, d = {0:-1 , 2:0 , 6:6}
                        
eleetminicoworoep       res = 5 (substring "leetm")
       ↑                

eleetminicoworoep       state = 6^4 = 00110 ^ 00100 = 00010 = 2
        ↑               seen this state  before, at index 0 , res = 8 - 0 = 8 (substring "leetmini")

eleetminicoworoep       state doesn't change , res = 9 (substring "leetminic")
         ↑ 

eleetminicoworoep       state = 2 ^ 8 = 00010^01000 = 01010 = 10 , res = 9 (substring "leetminic")
          ↑             d = {0:-1 , 2:0 , 10:10}

eleetminicoworoep       state doesn't change , res = 9 (substring "leetminic")
           ↑ 

eleetminicoworoep       state = 10^8 = 01010^01000 = 2 , res = 12-d[2]= 12 (substring "leetminicowo")
            ↑

eleetminicoworoep       state doesn't change , res = 13 (substring "leetminicowor")
             ↑

eleetminicoworoep       state = 2^8 = 10 , res doesn't change = 13 (substring "leetminicowor")
              ↑

eleetminicoworoep       state = 10^2 = 8 ->d = {0:-1 , 2:0 , 10:10 ,8:15}
               ↑        res doesn't change = 13 (substring "leetminicowor")

eleetminicoworoep       state doesn't change , res doesn't change #res=13 (substring "leetminicowor")
                ↑
'''
