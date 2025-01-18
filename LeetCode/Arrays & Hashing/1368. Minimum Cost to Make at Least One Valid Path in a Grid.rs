// Given an m x n grid. Each cell of the grid has a sign pointing to the next cell you should visit if you are currently in this cell. The sign of grid[i][j] can be:
// 1 which means go to the cell to the right. (i.e go from grid[i][j] to grid[i][j + 1])
// 2 which means go to the cell to the left. (i.e go from grid[i][j] to grid[i][j - 1])
// 3 which means go to the lower cell. (i.e go from grid[i][j] to grid[i + 1][j])
// 4 which means go to the upper cell. (i.e go from grid[i][j] to grid[i - 1][j])
// Notice that there could be some signs on the cells of the grid that point outside the grid.
// You will initially start at the upper left cell (0, 0). A valid path in the grid is a path that starts from the upper left cell (0, 0) 
// and ends at the bottom-right cell (m - 1, n - 1) following the signs on the grid. The valid path does not have to be the shortest.
// You can modify the sign on a cell with cost = 1. You can modify the sign on a cell one time only.
// Return the minimum cost to make the grid have at least one valid path.

// Example 1:
// ->->->->
// <-<-<-<-
// ->->->->
// <-<-<-<-
// Input: grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
// Output: 3
// Explanation: You will start at point (0, 0).
// The path to (3, 3) is as follows. (0, 0) --> (0, 1) --> (0, 2) --> (0, 3) change the arrow to down with cost = 1 --> (1, 3) --> (1, 2) --> (1, 1) --> (1, 0) 
// change the arrow to down with cost = 1 --> (2, 0) --> (2, 1) --> (2, 2) --> (2, 3) change the arrow to down with cost = 1 --> (3, 3)
// The total cost = 3.

// Example 2:
// Input: grid = [[1,1,3],[3,2,2],[1,1,4]]  Output: 0  Explanation: You can follow the path from (0, 0) to (2, 2).

// Example 3:
// Input: grid = [[1,2],[4,3]] Output: 1
 
// Constraints:
// m == grid.length
// n == grid[i].length
// 1 <= m, n <= 100
// 1 <= grid[i][j] <= 4

use std::collections::VecDeque;

impl Solution {
    pub fn min_cost(grid: Vec<Vec<i32>>) -> i32 {
        let rows = grid.len();
        let cols = grid[0].len();
        let mut minCost = vec![vec![i32::MAX ; cols] ; rows];
        minCost[0][0] = 0;
        let mut q = VecDeque::new();
        q.push_front((0 , 0));
        let directions = [(0,1) , (0,-1) , (1,0) , (-1,0)]; //right, left, down, up
        
        while let Some((r , c)) = q.pop_front(){
            for (i , &(dr , dc)) in directions.iter().enumerate() {
                let new_r = r as i32 + dr; // r and c are originally usize (usize required for array indexing)
                let new_c = c as i32 + dc;
                if new_r>= 0 && new_r<rows as i32 && new_c>=0 && new_c<cols as i32 {
                    let new_r = new_r as usize;
                    let new_c = new_c as usize;
                    let cost = if grid[r][c] != (i as i32 + 1) { 1 } else { 0 };
                    if minCost[r][c] + cost < minCost[new_r][new_c] {
                        minCost[new_r][new_c] = minCost[r][c] + cost;
                        if cost == 0 {
                            q.push_front((new_r , new_c));
                        }else {
                            q.push_back((new_r , new_c));
                        }
                    }
                }
            }
        }
        minCost[rows -1][cols -1]

        // println!("{:?}",minCost);
        // println!("{:?}",q);
        // println!("{:?}",directions);
        // 0
    }
}
