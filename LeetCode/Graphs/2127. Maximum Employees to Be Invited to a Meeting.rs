// A company is organizing a meeting and has a list of n employees, waiting to be invited. They have arranged for a large circular table, capable of seating any number of employees.
// The employees are numbered from 0 to n - 1. Each employee has a favorite person and they will attend the meeting only if they can sit next to their favorite person at the table. The favorite person of an employee is not themself.
// Given a 0-indexed integer array favorite, where favorite[i] denotes the favorite person of the ith employee, 
// return the maximum number of employees that can be invited to the meeting.

// Example 1:
//   1 <----> 2   <---3
//     table  ^
//           /
//          0
// Input: favorite = [2,2,1,2]
// Output: 3
// Explanation:
// The above figure shows how the company can invite employees 0, 1, and 2, and seat them at the round table.
// All employees cannot be invited because employee 2 cannot sit beside employees 0, 1, and 3, simultaneously.
// Note that the company can also invite employees 1, 2, and 3, and give them their desired seats.
// The maximum number of employees that can be invited to the meeting is 3. 

// Example 2:
//   0 -------> 1
//   ^  table   |
//    \        /
//      -- 2 <-
// Input: favorite = [1,2,0]
// Output: 3
// Explanation: 
// Each employee is the favorite person of at least one other employee, and the only way the company can invite them is if they invite every employee.
// The seating arrangement will be the same as that in the figure given in example 1:
// - Employee 0 will sit between employees 2 and 1.
// - Employee 1 will sit between employees 0 and 2.
// - Employee 2 will sit between employees 1 and 0.
// The maximum number of employees that can be invited to the meeting is 3.

// Example 3:
// Input: favorite = [3,0,1,4,1]
// Output: 4
// Explanation:
// The above figure shows how the company will invite employees 0, 1, 3, and 4, and seat them at the round table.
// Employee 2 cannot be invited because the two spots next to their favorite employee 1 are taken.
// So the company leaves them out of the meeting.
// The maximum number of employees that can be invited to the meeting is 4.
 
// Constraints:
// n == favorite.length
// 2 <= n <= 10**5
// 0 <= favorite[i] <= n - 1
// favorite[i] != i

use std::collections::{HashSet , VecDeque , HashMap};
impl Solution {
    pub fn maximum_invitations(favorite: Vec<i32>) -> i32 {
        // find max cycle length (Cycle with size > 2)
        fn get_max_cycle_length(fav : &Vec<i32>) -> i32 {
            let person_count = fav.len();
            let mut max_cycle_length = 0;
            let mut visited = HashSet::new();
            for i in 0..person_count {
                let i = i as i32;
                if !visited.contains(&i) {
                    let mut start_person = i ;
                    let mut cur_visited = HashSet::new();
                    let mut cur_person = i ;
                    while !visited.contains(&cur_person) { // try to find cycle
                        visited.insert(cur_person);
                        cur_visited.insert(cur_person);
                        cur_person = fav[cur_person as usize];
                    }
                    if cur_visited.contains(&cur_person){  // Cycle detected
                        let mut cur_cycle_length = cur_visited.len() as i32 ;
                        while start_person != cur_person {
                            cur_cycle_length -= 1 ;
                            start_person = fav[start_person as usize] ;
                        }
                        max_cycle_length = max_cycle_length.max(cur_cycle_length);
                    }
                }
            }
            max_cycle_length
        }

        fn bfs(graph: &HashMap<i32 , Vec<i32>>, node:i32 , dest:i32)->i32{
            let mut q = VecDeque::new();
            q.push_back((node , 0)); // node , length
            let mut max_length = 0 ;
            while let Some((node ,length)) = q.pop_front() {
                if node != dest {
                    max_length = max_length.max(length);
                    if let Some(neighbors) = graph.get(&node){
                        for &nei in neighbors {
                            q.push_back((nei , length+ 1));
                        }
                    }
                }
            }
            max_length
        }
        // find longest path ((Cycle with size == 2) + extended paths)
        fn get_longest_path(fav: &Vec<i32>) -> i32 {
            let mut pairs = Vec::new();
            let mut visited = HashSet::new();
            let n_persons = fav.len(); // usize by default

            //find cycle with size == 2 (a<-->b) pairs
            for i in 0..n_persons { // i is usize
                if !visited.contains(&(i as i32)) && fav[fav[i] as usize] == i as i32{
                    pairs.push((i as i32 , fav[i]));
                    visited.insert(i as i32);
                    visited.insert(fav[i]);
                }
            }
            // println!("{:?}", visited);
            // println!("{:?}", pairs);
            // 0 

            //build adjacency list (graph)
            let mut graph : HashMap<i32 , Vec<i32>> = HashMap::new();
            for (node , &destination) in fav.iter().enumerate() { // node is usize , destination is i32
                if let Some(vec) = graph.get_mut(&destination) {
                    vec.push(node as i32);
                } else {
                    graph.insert(destination, vec![node as i32]);
                }
            }
            // println!("{:?}", graph);
            // 0 

            //cal longest path
            let mut longest_path = 0 ;
            for (person1 , person2) in pairs {
                longest_path += 2 + bfs(&graph , person1 , person2) + bfs(&graph , person2 , person1); // (Cycle with size == 2) + extended paths
            }
            longest_path
        }
        
        let max_cycle_length = get_max_cycle_length(&favorite);
        let longest_path = get_longest_path(&favorite);
        max_cycle_length.max(longest_path)
    }
}
