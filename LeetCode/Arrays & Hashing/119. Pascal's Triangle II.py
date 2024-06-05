Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:
Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:
Input: rowIndex = 0
Output: [1]

Example 3:
Input: rowIndex = 1
Output: [1,1]
 
Constraints:  0 <= rowIndex <= 33

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
        
