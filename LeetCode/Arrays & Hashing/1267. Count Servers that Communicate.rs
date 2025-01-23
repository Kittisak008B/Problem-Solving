// You are given a map of a server center, represented as a m*n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. 
// Two servers are said to communicate if they are on the same row or on the same column. Return the number of servers that communicate with any other server.

// Example 1:
// 1 0
// 0 1
// Input: grid = [[1,0],[0,1]]
// Output: 0   Explanation: No servers can communicate with others.

// Example 2:
// 1 0
// 1 1
// Input: grid = [[1,0],[1,1]]
// Output: 3   Explanation: All three servers can communicate with at least one other server.

// Example 3:
// 1 1 0 0
// 0 0 1 0
// 0 0 1 0
// 0 0 0 1
// Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
// Output: 4
// Explanation: The two servers in the first row can communicate with each other. 
// The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.
 
// Constraints:
// m == grid.length
// n == grid[i].length
// 1 <= m <= 250
// 1 <= n <= 250
// grid[i][j] == 0 or 1

impl Solution {
    pub fn count_servers(grid: Vec<Vec<i32>>) -> i32 {
        let rows = grid.len();
        let cols = grid[0].len();
        let mut count_r = vec![0 ; rows];
        let mut count_c = vec![0 ; cols];
        for r in 0..rows {
            for c in 0..cols{
                if grid[r][c] == 1 {
                    count_r[r] += 1;
                    count_c[c] += 1;
                }
            }
        }
        // println!("{:?}", count_r);
        // println!("{:?}", count_c);
        // 0
        let mut res = 0 ;
        for r in 0..rows{
            for c in 0..cols {
                if grid[r][c] == 1 && (count_r[r] >= 2 || count_c[c] >= 2) {
                    res += 1;
                }
         
            }
        }
        res
    }
}
