// Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.

// Example 1:
// Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
// Output: 4
// Explanation: After the rain, water is trapped between the blocks.
// We have two small ponds 1 and 3 units trapped. The total volume of water trapped is 4.

// Example 2:
// Input: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
// Output: 10
 
// Constraints:
// m == heightMap.length
// n == heightMap[i].length
// 1 <= m, n <= 200
// 0 <= heightMap[i][j] <= 2 * 10**4

use std::collections::BinaryHeap; // max-heap by default
use std::cmp::Reverse;  //for convert Rust's max-heap into a min-heap
impl Solution {
    pub fn trap_rain_water(height_map: Vec<Vec<i32>>) -> i32 {
        // cells cannot trap the water
        if height_map.is_empty() || height_map[0].is_empty(){
            return 0;
        }
        let (m , n) = (height_map.len() , height_map[0].len());
        if m < 3 || n < 3 {
            return 0;
        }

        // Push border cells into heap
        let mut heap = BinaryHeap::new(); 
        let mut visited = vec![vec![false ; n] ; m];
        for i in 0..m{
            for j in 0..n{
                if i==0 || i==m-1 || j==0 || j==n-1 {
                    heap.push( Reverse((height_map[i][j] , i , j)) );
                    visited[i][j] = true;
                }
            }
        }
        // println!("{:?}", heap);
        // println!("{:?}", visited);
        // 0

        let directions = [(-1, 0), (1, 0), (0, -1), (0, 1)];
        let mut level = 0;
        let mut res = 0;
        while let Some(Reverse((height , x , y))) = heap.pop() {
            level = level.max(height);
            for &(dx , dy) in &directions {
                let (new_x , new_y) = (x as isize + dx , y as isize + dy);
                if new_x >= 0 && new_x < m as isize && new_y >= 0 && new_y < n as isize {
                    let (new_x, new_y) = (new_x as usize, new_y as usize);
                    if !visited[new_x][new_y] {
                        heap.push(Reverse((height_map[new_x][new_y], new_x, new_y)));
                        if height_map[new_x][new_y] < level {
                            res += level - height_map[new_x][new_y];
                        }
                        visited[new_x][new_y] = true;
                    }
                }
            }
        }
        res
    }
}
