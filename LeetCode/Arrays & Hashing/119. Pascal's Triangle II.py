# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle. In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
#       1
#      1 1
#     1 2 1
#    1 3 3 1
#   1 4 6 4 1

# Example 1:
# Input: rowIndex = 3
# Output: [1,3,3,1]

# Example 2:
# Input: rowIndex = 0
# Output: [1]

# Example 3:
# Input: rowIndex = 1
# Output: [1,1]
 
# Constraints:  0 <= rowIndex <= 33

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0 :
            return [1]
        prev_row = self.getRow(rowIndex - 1)
        cur_row = [1]
        for i in range(len(prev_row)-1) :
            cur_row.append(prev_row[i] + prev_row[i+1])
        cur_row.append(1)
        return cur_row

# class Solution:
#     def getRow(self, rowIndex: int) -> List[int]:
#         ans = [1]
#         for i in range(rowIndex) :
#             ans.append(1)
#             for j in range(len(ans)-2 , 0 , -1) :
#                 ans[j] += ans[j-1]
#         return ans
'''
rowindex = 5
i=0 [1,1]
i=1 [1,1+1,1] -> [1,2,1] 
i=2 [1,2+1,1+2,1] -> [1,3,3,1]  
i=3 [1,3+1,3+3,1+3,1] -> [1,4,6,4,1]
i=4 [1,4+1,6+4,4+6,1+4,1] -> [1,5,10,10,5,1]
'''
