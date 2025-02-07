// You are given an integer limit and a 2D array queries of size n x 2.
// There are limit + 1 balls with distinct labels in the range [0, limit]. 
// Initially, all balls are uncolored. For every query in queries that is of the form [x, y], you mark ball x with the color y.
// After each query, you need to find the number of distinct colors among the balls.
// Return an array result of length n, where result[i] denotes the number of distinct colors after ith query.
// Note that when answering a query, lack of a color will not be considered as a color.

// Example 1:
// Input: limit = 4, queries = [[1,4],[2,5],[1,3],[3,4]]
// Output: [1,2,2,3]
// Explanation:
// After query 0, ball 1 has color 4.
// After query 1, ball 1 has color 4, and ball 2 has color 5.
// After query 2, ball 1 has color 3, and ball 2 has color 5.
// After query 3, ball 1 has color 3, ball 2 has color 5, and ball 3 has color 4.

// Example 2:
// Input: limit = 4, queries = [[0,1],[1,2],[2,2],[3,4],[4,5]]
// Output: [1,2,2,3,4]
// Explanation:
// After query 0, ball 0 has color 1.
// After query 1, ball 0 has color 1, and ball 1 has color 2.
// After query 2, ball 0 has color 1, and balls 1 and 2 have color 2.
// After query 3, ball 0 has color 1, balls 1 and 2 have color 2, and ball 3 has color 4.
// After query 4, ball 0 has color 1, balls 1 and 2 have color 2, ball 3 has color 4, and ball 4 has color 5.
 
// Constraints:
// 1 <= limit <= 10**9
// 1 <= n == queries.length <= 10**5
// queries[i].length == 2
// 0 <= queries[i][0] <= limit
// 1 <= queries[i][1] <= 10**9

use std::collections::HashMap;
impl Solution {
    pub fn query_results(limit: i32, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let mut colors = HashMap::new();
        let mut balls = HashMap::new();
        let mut res = vec![];
        for q in queries.iter() { //q is &Vec<i32>
            let ball = q[0]; //i32
            let color = q[1];
            if let Some(&prev_ball_color) = balls.get(&ball){
                if let Some(count) = colors.get_mut(&prev_ball_color){ //count is &mut i32
                    *count -= 1;
                    if *count == 0 {
                        colors.remove(&prev_ball_color);
                    }
                }
            }
            *colors.entry(color).or_insert(0) += 1; //.or_insert(0) returns a mutable reference (&mut i32)
            balls.insert(ball , color);
            res.push(colors.len() as i32);
        }
        res 
    }
}
