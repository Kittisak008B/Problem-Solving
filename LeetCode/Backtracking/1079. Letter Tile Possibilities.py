# You have n  tiles, where each tile has one letter tiles[i] printed on it.
# Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

# Example 1:
# Input: tiles = "AAB"
# Output: 8
# Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".

# Example 2:
# Input: tiles = "AAABBC"
# Output: 188

# Example 3:
# Input: tiles = "V"
# Output: 1
 
# Constraints:
# 1 <= tiles.length <= 7
# tiles consists of uppercase English letters.

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def backtrack(freq) :
            count = 0
            for i in range(26) :
                if not freq[i] :
                    continue
                freq[i] -= 1
                count += 1
                count += backtrack(freq) 
                freq[i] += 1
            return count
        freq = [0] * 26
        for char in tiles :
            freq[ord(char) - ord('A')] += 1  
        return backtrack(freq)
      
