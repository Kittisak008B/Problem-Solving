// You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) represents:
// A land cell if grid[r][c] = 0, or
// A water cell containing grid[r][c] fish, if grid[r][c] > 0.
// A fisher can start at any water cell (r, c) and can do the following operations any number of times:
// Catch all the fish at cell (r, c), or
// Move to any adjacent water cell.
// Return the maximum number of fish the fisher can catch if he chooses his starting cell optimally, or 0 if no water cell exists.
// An adjacent cell of the cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) or (r - 1, c) if it exists.

// Example 1:
// 0 2 1 0
// 4 0 0 3
// 1 0 0 4
// 0 3 2 0
// Input: grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
// Output: 7
// Explanation: The fisher can start at cell (1,3) and collect 3 fish, then move to cell (2,3) and collect 4 fish.
  
// Example 2:
// Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]
// Output: 1
// Explanation: The fisher can start at cells (0,0) or (3,3) and collect a single fish. 

// Constraints:
// m == grid.length
// n == grid[i].length
// 1 <= m, n <= 10
// 0 <= grid[i][j] <= 10

use std::collections::HashSet;

impl Solution {
    pub fn find_max_fish(grid: Vec<Vec<i32>>) -> i32 {

        fn dfs(r:usize, c:usize, visited:&mut HashSet<(usize,usize)>, grid:&Vec<Vec<i32>>, rows:usize, cols:usize) -> i32{
            if r<0 || r>= rows || c<0 || c>= cols || grid[r][c] == 0 || visited.contains(&(r,c)) {
                return 0;
            }
            let mut total_fish = grid[r][c];
            visited.insert((r , c));
            let directions = [(1, 0), (-1, 0), (0, 1), (0, -1)];
            for &(dr , dc) in directions.iter(){
                let new_r = r as i32 + dr;
                let new_c = c as i32 + dc;
                total_fish += dfs(new_r as usize , new_c as usize , visited , grid , rows , cols);
            }
            total_fish
        }        
        let rows = grid.len() ;
        let cols = grid[0].len() ;
        let mut res = 0;
        let mut visited = HashSet::new();
        for r in 0..rows {
            for c in 0..cols {
                if grid[r][c] > 0 && !visited.contains(&(r,c)) {
                    res = res.max(dfs(r , c ,&mut visited , &grid , rows , cols));
                }
            }
        }
        res
    }
}
