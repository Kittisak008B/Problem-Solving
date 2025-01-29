// In this problem, a tree is an undirected graph that is connected and has no cycles.
// You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. 
// The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. 
// The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.
// Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

// Example 1:
//    1--2
//    | / 
//    3
// Input: edges = [[1,2],[1,3],[2,3]]
// Output: [2,3]

// Example 2:
//    2--1--5
//    |  |
//    3--4
// Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
// Output: [1,4]
 
// Constraints:   
// edges[i].length == 2   
// 1 <= ai < bi <= edges.length    ai != bi
// There are no repeated edges.    The given graph is connected.

impl Solution {
    pub fn find_redundant_connection(edges: Vec<Vec<i32>>) -> Vec<i32> {
        struct UnionFind{
            parent : Vec<usize>,
            rank : Vec<usize>,
        }
        impl UnionFind {
            fn new(size: usize) -> Self{
                Self{
                    parent: (0..size).collect(),
                    rank: vec![0 ; size],
                }
            }
            fn find_par(&mut self , x:usize) -> usize{
                if self.parent[x] != x {
                    self.parent[x] = self.find_par(self.parent[x]);
                }
                self.parent[x]
            }
            fn union(&mut self, x:usize , y:usize)->bool{
                let par_x = self.find_par(x);
                let par_y = self.find_par(y);
                if par_x == par_y {
                    return false;
                }
                if self.rank[par_x] > self.rank[par_y] {
                    self.parent[par_y] = par_x ;
                } else if self.rank[par_y] > self.rank[par_x] {
                    self.parent[par_x] = par_y ;
                } else {
                    self.parent[par_x] = par_y ;
                    self.rank[par_y] += 1 ;
                }
                true
            } 
        }
        let mut uf = UnionFind::new(edges.len() + 1);
        for edge in edges.iter() {  // Use for edge in edges.iter() (or for edge in &edges) when: You want to borrow the elements (&Vec<i32>) instead of taking ownership.
            let x = edge[0] as usize;
            let y = edge[1] as usize;
            if uf.union(x , y) == false {
                return vec![edge[0], edge[1]];
            }
        }
        vec![]
    }
}
