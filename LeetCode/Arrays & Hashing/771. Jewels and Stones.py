# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. 
# Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
# Letters are case sensitive, so "a" is considered a different type of stone from "A".

# Example 1:
# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3

# Example 2:
# Input: jewels = "z", stones = "ZZ"
# Output: 0
 
# Constraints:  jewels and stones consist of only English letters.  All the characters of jewels are unique.

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        jewels_set = set()
        for char in jewels :
            jewels_set.add(char)

        for char in stones :
            if char in jewels_set :
                ans += 1
        return ans
      
