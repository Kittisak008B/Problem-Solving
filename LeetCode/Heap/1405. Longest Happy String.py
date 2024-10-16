# A string s is called happy if it satisfies the following conditions:
# s only contains the letters 'a', 'b', and 'c'.
# s does not contain any of "aaa", "bbb", or "ccc" as a substring.
# s contains at most a occurrences of the letter 'a'.
# s contains at most b occurrences of the letter 'b'.
# s contains at most c occurrences of the letter 'c'.
# Given three integers a, b, and c, return the longest possible happy string. 
# If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".
# A substring is a contiguous sequence of characters within a string.

# Example 1:
# Input: a = 1, b = 1, c = 7
# Output: "ccaccbcc"
# Explanation: "ccbccacc" would also be a correct answer.

# Example 2:
# Input: a = 7, b = 1, c = 0
# Output: "aabaa"
# Explanation: It is the only correct answer in this case.
 
# Constraints:
# 0 <= a, b, c <= 100
# a + b + c > 0

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        d = {'a':a ,'b':b ,'c':c}
        heap = []
        for key , val in d.items() :
            if val != 0 :
                heap.append((-val , key))
        heapq.heapify(heap)
        res = ''
        while heap :
            count , char = heapq.heappop(heap)
            if len(res) > 1 and res[-1] == res[-2] == char :
                if not heap :
                    break
                count2 , char2 = heapq.heappop(heap)
                res += char2
                if count2 != -1 :
                    heapq.heappush(heap,(count2 +1 , char2))
                heapq.heappush(heap,(count , char))
            else:
                res += char
                if count != -1 :
                    heapq.heappush(heap,(count +1 , char))
        return res
'''
# Example 1:
# Input: a = 1, b = 1, c = 7
# Output: "ccaccbcc"

[(-7, 'c'), (-1, 'b'), (-1, 'a')]
[(-6, 'c'), (-1, 'b'), (-1, 'a')]
[(-5, 'c'), (-1, 'b'), (-1, 'a')]
[(-5, 'c'), (-1, 'b')]
[(-4, 'c'), (-1, 'b')]
[(-3, 'c'), (-1, 'b')]
[(-3, 'c')]
[(-2, 'c')]
[(-1, 'c')]
'''
