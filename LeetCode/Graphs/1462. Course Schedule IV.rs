// There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
// You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course ai first if you want to take course bi.
// For example, the pair [0, 1] indicates that you have to take course 0 before you can take course 1.
// Prerequisites can also be indirect. If course a is a prerequisite of course b, and course b is a prerequisite of course c, then course a is a prerequisite of course c.
// You are also given an array queries where queries[j] = [uj, vj]. For the jth query, you should answer whether course uj is a prerequisite of course vj or not.
// Return a boolean array answer, where answer[j] is the answer to the jth query.

// Example 1:
// 1->0
// Input: numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
// Output: [false,true]
// Explanation: The pair [1, 0] indicates that you have to take course 1 before you can take course 0.
// Course 0 is not a prerequisite of course 1, but the opposite is true.

// Example 2:
// Input: numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]
// Output: [false,false]
// Explanation: There are no prerequisites, and each course is independent.
  
// Example 3:
// 1-> 0
// \   ^
//  v /
//   2
// Input: numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
// Output: [true,true]
 
// Constraints:
// 2 <= numCourses <= 100
// 0 <= prerequisites.length <= (numCourses * (numCourses - 1) / 2)
// prerequisites[i].length == 2
// 0 <= ai, bi <= numCourses - 1
// ai != bi
// All the pairs [ai, bi] are unique.
// The prerequisites graph has no cycles.
// 1 <= queries.length <= 10**4
// 0 <= ui, vi <= numCourses - 1
// ui != vi

use std::collections::{HashSet , HashMap};
impl Solution {
    pub fn check_if_prerequisite(num_courses: i32, prerequisites: Vec<Vec<i32>>, queries: Vec<Vec<i32>>) -> Vec<bool> {
        let mut graph : HashMap<i32 , Vec<i32>> = HashMap::new();
        for pairs in prerequisites.iter(){ // `pairs` is borrowed as &Vec<i32>
            let (pre , node) = (pairs[0] , pairs[1]);
            if let Some(vec) = graph.get_mut(&node){
                vec.push(pre);
            } else {
                graph.insert(node , vec![pre]);
            }
        }
        // println!("{:?}" , graph);
        fn dfs(node: i32 , graph: &HashMap<i32 , Vec<i32>> , map: &mut HashMap<i32 , HashSet<i32>>) -> HashSet<i32> {
            if !map.contains_key(&node){
                let mut temp_set = HashSet::new();
                if let Some(pre_list) = graph.get(&node) {
                    for &pre in pre_list {
                        let for_union_set = dfs(pre, graph , map);
                        temp_set.extend(for_union_set); // Union of sets
                    }
                }
                temp_set.insert(node);
                map.insert(node , temp_set);
            }
            match map.get(&node) {
                Some(set) => set.clone(),
                None => HashSet::new(),// node wasn't found , return an empty set
            }
        }
        let mut map : HashMap<i32 , HashSet<i32>> = HashMap::new() ; 
        for node in 0..num_courses {
            dfs(node , &graph , &mut map);
        }
        let mut res = Vec::new();
        for querie in queries.iter() {
            let (node1 , node2) = (querie[0] , querie[1]);
            if let Some(set) = map.get(&node2) {
                res.push(set.contains(&node1));
            } else {
                res.push(false);
            }
        }
        res
        // vec![true]
    }
}
