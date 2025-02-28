# Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.
# A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.

# Example 1:
# Input: str1 = "abac", str2 = "cab"
# Output: "cabac"
# Explanation: 
# str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
# str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
# The answer provided is the shortest such string that satisfies these properties.
  
# Example 2:
# Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
# Output: "aaaaaaaa"
 
# Constraints:
# 1 <= str1.length, str2.length <= 1000
# str1 and str2 consist of lowercase English letters.

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
      
        #Bottom-Up Dynamic Programming    Backtracking ->Time Limit Exceeded , Memoization -> Memory Limit Exceeded
        str1_length, str2_length = len(str1), len(str2)
        # Initialize the first row: when str1 is empty, the supersequence is just the prefix of str2
        prev_row = [str2[:col] for col in range(str2_length + 1)]
        for row in range(1, str1_length + 1):
            # Initialize the first column: when str2 is empty, the supersequence is just the prefix of str1
            curr_row = [str1[:row]] + [None] * str2_length
            for col in range(1, str2_length + 1):
                if str1[row - 1] == str2[col - 1]:  # If characters match, extend the supersequence
                    curr_row[col] = prev_row[col - 1] + str1[row - 1]
                else:  # If characters don't match, choose the shorter supersequence
                    pick_s1 = prev_row[col] + str1[row - 1]  # Extend with str1[row-1]
                    pick_s2 = curr_row[col - 1] + str2[col - 1]  # Extend with str2[col-1]
                    curr_row[col] = min(pick_s1, pick_s2, key=len)  # Pick the shorter one
            prev_row = curr_row  # Move to the next row
        return prev_row[str2_length]  # The last cell contains the shortest common supersequence
