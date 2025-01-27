// Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

// Example 1:
// Input: arr = [1,2,2,1,1,3]
// Output: true
// Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

// Example 2:
// Input: arr = [1,2]
// Output: false

// Example 3:
// Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
// Output: true
 
// Constraints:
// 1 <= arr.length <= 1000
// -1000 <= arr[i] <= 1000

use std::collections::{HashMap , HashSet};

impl Solution {
    pub fn unique_occurrences(arr: Vec<i32>) -> bool {
        let mut d = HashMap::new();
        for num in arr { // `num` is of type `i32`
            if let Some(count) = d.get_mut(&num){ // `d.get_mut(&num)` returns `Option<&mut i32>`
                *count += 1;  // `count` is `&mut i32`, so we dereference (`*count`) and increment
            } else {
                d.insert(num , 1);
            }
        }
        let mut occur_set = HashSet::new();
        for &count in d.values(){  // `d.values()` produces `&i32`, `&count` dereferences to `i32`
            if occur_set.contains(&count){ // `.contains(&count)` expects `&i32`
                return false
            } else {
                occur_set.insert(count);
            }
        }
        true
    }
}
