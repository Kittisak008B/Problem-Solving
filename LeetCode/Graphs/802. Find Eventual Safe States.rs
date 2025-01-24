// There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array graph where 
// graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].
// A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).
// Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.
  
// Example 1:
//           +---------------------------+
//           |                           |
//           v                           |
//         +----+        +----+        +----+
//         | 0  | ---->  | 1  | ---->  | 3  |
//         +----+        +----+        +----+
//           |              |             
//           |  +-----------+  
//           |  |              
//           v  v             
//        +----+       +----+     +----+
//        | 2  | ----> | 5  |     | 6  |   (node 5 , node 6 : No outgoing edges)
//        +----+       +----+     +----+
//                       ^
//                       |   
//                     +----+
//                     | 4  |
//                     +----+
// Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
// Output: [2,4,5,6]
// Explanation: The given graph is shown above. Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
// Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.

// Constraints:
// n == graph.length
// 1 <= n <= 10**4
// 0 <= graph[i].length <= n
// 0 <= graph[i][j] <= n - 1
// graph[i] is sorted in a strictly increasing order.
// The graph may contain self-loops.
// The number of edges in the graph will be in the range [1, 4 * 10**4].

use std::collections::HashMap;

impl Solution {
    pub fn eventual_safe_nodes(graph: Vec<Vec<i32>>) -> Vec<i32> {
        let mut dp: HashMap<i32 , bool> = HashMap::new(); 

        fn dfs(node: i32, graph: &Vec<Vec<i32>>, dp: &mut HashMap<i32, bool>) -> bool{
            if let Some(&val) = dp.get(&node){
                return val; 
            }
            dp.insert(node, false); 
            for &neighbor in &graph[node as usize] {
                if dfs(neighbor, graph, dp) == false {
                    return dfs(node, graph, dp); 
                }
            }
            dp.insert(node, true); 
            true
        }
        let mut res = Vec::new();
        for i in 0..graph.len() as i32 {
            if dfs(i, &graph, &mut dp) {
                res.push(i); 
            }
        }
        res
    }
}
