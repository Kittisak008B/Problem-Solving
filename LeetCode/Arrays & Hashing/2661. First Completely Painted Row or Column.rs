// You are given a 0-indexed integer array arr, and an m x n integer matrix mat. arr and mat both contain all the integers in the range [1, m * n].
// Go through each index i in arr starting from index 0 and paint the cell in mat containing the integer arr[i].
// Return the smallest index i at which either a row or a column will be completely painted in mat.

// Example 1:
// 14 -> #4  -> #4 -> ## 
// 23    23     2#    2#
// Input: arr = [1,3,4,2], mat = [[1,4],[2,3]]
// Output: 2    Explanation: The moves are shown in order, and both the first row and second column of the matrix become fully painted at arr[2].

// Example 2:
// 325    3#5    3#5    3#5    3#5
// 146 -> 146 -> 146 -> 146 -> 1#6
// 879    879    #79    ##9    ##9
// Input: arr = [2,8,7,4,1,3,5,6,9], mat = [[3,2,5],[1,4,6],[8,7,9]]
// Output: 3    Explanation: The second column becomes fully painted at arr[3].
 
// Constraints:
// m == mat.length
// n = mat[i].length
// arr.length == m * n
// 1 <= m, n <= 10**5
// 1 <= m * n <= 10**5
// 1 <= arr[i], mat[r][c] <= m * n
// All the integers of arr are unique.
// All the integers of mat are unique.

use std::collections::HashMap;

impl Solution {
    pub fn first_complete_index(arr: Vec<i32>, mat: Vec<Vec<i32>>) -> i32 {
        let rows = mat.len();
        let cols = mat[0].len();
        let mut d:HashMap<i32 , (usize , usize)> = HashMap::new();
        for i in 0..rows{
            for j in 0..cols{
                d.insert(mat[i][j] , (i , j));
            }
        }
        let mut row_freq = vec![0 ; rows];
        let mut col_freq = vec![0 ; cols];
        for (i , &num) in arr.iter().enumerate() {
            if let Some(&(r , c)) = d.get(&num) {
                row_freq[r] += 1;
                col_freq[c] += 1;
                if row_freq[r] == cols || col_freq[c] == rows {
                    return i as i32
                }
            }
        }
        -1
    }
}
