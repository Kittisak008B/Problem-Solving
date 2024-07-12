# You are given a string s and two integers x and y. You can perform two types of operations any number of times.
# Remove substring "ab" and gain x points. For example, when removing "ab" from "cabxbae" it becomes "cxbae".
# Remove substring "ba" and gain y points. For example, when removing "ba" from "cabxbae" it becomes "cabxe".
# Return the maximum points you can gain after applying the above operations on s.

# Example 1:
# Input: s = "cdbcbbaaabab", x = 4, y = 5
# Output: 19
# Explanation:
# - Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
# - Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
# - Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
# - Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
# Total score = 5 + 4 + 5 + 5 = 19.

# Example 2:
# Input: s = "aabbaaxybbaabb", x = 5, y = 4
# Output: 20
 
# Constraints: 1 <= s.length <= 105    1 <= x, y <= 104    s consists of lowercase English letters.

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def cal_substring2_in_stack(stack , val) :
            count_a , count_b = 0 , 0
            for c in stack :
                if c == 'a' :
                    count_a += 1
                else :
                    count_b += 1
            return min(count_a , count_b) * val
        stack = []
        ans = 0
        if x > y :
            substring_1 = 'ab'
        else :
            substring_1 = 'ba'
        for c in s :
            if stack and c == substring_1[1] and stack[-1] == substring_1[0] :
                stack.pop()
                ans += max(x , y)
            elif c == substring_1[0] or c == substring_1[1] :
                stack.append(c)
            else :
                ans += cal_substring2_in_stack(stack , min(x , y)) 
                for _ in range(len(stack)) :
                    stack.pop()
        if stack :
            ans += cal_substring2_in_stack(stack , min(x , y))
        return ans
      
