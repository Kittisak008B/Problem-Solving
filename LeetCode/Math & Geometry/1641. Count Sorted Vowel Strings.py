# Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.
# A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.

# Example 1:
# Input: n = 1
# Output: 5
# Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].

# Example 2:
# Input: n = 2
# Output: 15
# Explanation: The 15 sorted strings that consist of vowels only are
# ["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
# Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.

# Example 3:
# Input: n = 33
# Output: 66045
 
# Constraints:  1 <= n <= 50 

class Solution:
    def countVowelStrings(self, n: int) -> int:
        def C(n , r) :
            return int(math.factorial(n) / (math.factorial(n - r)*math.factorial(r)))
        if n >= 1 and n < 5 :
            if n == 1 :
                return 5
            elif n == 2 :
                return 5 + C(5 , 2)*C(n-1 , 1)
            elif n == 3 :
                return 5 + C(5 , 2)*C(n-1 , 1) + C(5 , 3)*C(n-1 , 2) 
            elif n == 4 :
                return 5 + C(5 , 2)*C(n-1 , 1) + C(5 , 3)*C(n-1 , 2) + C(5 , 4)*C(n-1 , 3) 
        else :
            return 5 + C(5 , 2)*C(n-1 , 1) + C(5 , 3)*C(n-1 , 2) + C(5 , 4)*C(n-1 , 3) + C(5 , 5)*C(n-1 , 4)
'''
C(n,r) = n!/((n-r)!*r!)

n = 1  C(5,1) = 5!/4! = 5  (a e i o u)
n = 2  C(5,2) = (5!)/(3!*2!) = 5*4/2 = 10 (ae ai ao au ei eo eu io iu ou) 
                                       + 5 (aa ee ii oo uu) 
                                    total = 10 + 5 =  15 

n = 3  choose 1 vowel diff -> 5 (aaa eee iii ooo uuu)
       choose 2 vowel diff ->   ex. a-a-e -> one converting point to change a to e -> C(2,1)
                                C(5,2)*C(n-1,1)=C(5,2)*C(2,1) = 10*2 = 20 (ae+a ai+a ao+a au+a ei+e eo+e eu+e io+i iu+i ou+o
                                                                           ae+e ai+i ao+o au+u ei+i eo+o eu+u io+o iu+u ou+u )
       choose 3 vowel diff ->   ex.a-e-i -> two converting point to change a to e and e to i -> C(2,2)
                                C(5,3)*C(n-1,k-1)=C(5,3)*C(2,2) = 10 (aei aeo aio eio aeu aiu eiu aou eou iou)
       total = 5 + 20 + 10 = 35

n = 4  choose 1 vowel diff -> 5 (aaaa,eeee,iiii,oooo,uuuu)
       choose 2 vowel diff ->   a-a-e-e -> one converting point to change a to e -> C(3,1)
                                C(5,2)*C(n-1,2)=C(5,2)*C(3,1) = 30 (ae+aa ai+aa ao+aa au.. ei.. eo.. eu.. io.. iu.. ou..
                                                                    ae+ee ai+ii ao+oo au.. ei.. eo.. eu.. io.. iu.. ou..
                                                                    ae+ae ai+ai ao+ao au.. ei.. eo.. eu.. io.. iu.. ou..)
       choose 3 vowel diff -> a-a-e-i -> two converting point to change a to e and e to i -> C(3,2)
                              C(5,3)*C(n-1,k-1)=C(5,3)*C(3,2) = 30
       choose 4 vowel diff -> C(5,4)*C(n-1,k-1)=C(5,4)*C(3,3) = 5 (aeio aeiu aeou aiou eiou)
       total = 5 + 30 + 30 + 5 = 70
...
n = 50 : choose 1 vowel diff + choose 2 vowel diff + choose 3 vowel diff + choose 4 vowel diff + choose 5 vowel diff
                   5         + C(5 , 2)*C(n-1 , 1) + C(5 , 3)*C(n-1 , 2) + C(5 , 4)*C(n-1 , 3) + C(5 , 5)*C(n-1 , 4)

------------------------
                   5 + 10*(n-1)!/((n-1-1)!*1!) + 10*(n-1)!/((n-1-2)!*2!) + 5*(n-1)!/((n-1-3)!*3!) + (n-1)!/((n-1-4)!*4!)
                   5 + 10*(n-1)!/(n-2)!        + 5*(n-1)!/(n-3)!      + 5*(n-1)!/((n-4)!*3*2)     + (n-1)!/((n-5)!*4!)
                   5 + 10*(n-1)                + 5*(n-1)(n-2)         + 5*(n-1)(n-2)(n-3)/6       + (n-1)(n-2)(n-3)(n-4)/4!
                   5 + 10n - 10                + 5*(n**2 -3n + 2)     + 5*(n**3 -6n**2 +11n -6)/6 + (n**4 -10n**3 +35n**2 -50n +24)/4!
                       10n-5                   + 5n**2 -15n +10    +4*(5n**3 -30n**2 +55n -30)/4! + (n**4 -10n**3 +35n**2 -50n +24)/4!
                                     4!*(5n**2 -5n +5)/4! + (20n**3 -120n**2 + 220n -120 )/4!  + (n**4 -10n**3 +35n**2 -50n +24)/4!
                                     (120n**2 -120n +120 + 20n**3 - 120n**2 + 220n -120  + n**4 -10n**3 +35n**2 -50n +24 )/4!  
                                     (        -120n      + 20n**3           + 220n       + n**4 -10n**3 +35n**2 -50n +24 )/4!
                                     (n**4 + 10n**3 + 35n**2 +50n + 24)/4!
                                     (n+1)(n+2)(n+3)(n+4)/4!
------------------------
Combination with repetitions. C(n+k-1,k)   
                            ->choose to distribute n distinct objects into k categories
         5 vowels to choose ->C(5+k-1,k) = C(4+k,k) = (k+1)(k+2)(k+3)(k+4)/4!
'''
