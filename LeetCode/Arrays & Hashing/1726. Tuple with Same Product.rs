// Given an array nums of distinct positive integers, return the number of tuples (a, b, c, d) such that a * b = c * d 
// where a, b, c, and d are elements of nums, and a != b != c != d.

// Example 1:
// Input: nums = [2,3,4,6]
// Output: 8
// Explanation: There are 8 valid tuples:
// (2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
// (3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)

// Example 2:
// Input: nums = [1,2,4,5,10]
// Output: 16
// Explanation: There are 16 valid tuples:
// (1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
// (2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
// (2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,5,4)
// (4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)
 
// Constraints:
// 1 <= nums.length <= 1000
// 1 <= nums[i] <= 10**4
// All elements in nums are distinct.

use std::collections::HashMap;
impl Solution {
    pub fn tuple_same_product(nums: Vec<i32>) -> i32 {
        let mut d = HashMap::new();
        let mut res = 0;
        let N = nums.len();
        for i in 0..N{
            for j in (i+1)..N {
                let product = nums[i] * nums[j];
                *d.entry(product).or_insert(0) += 1;
            }
        }
        // println!("{:?}", d);
        for (&key , &val) in &d { //(&i32, &i32)
            if val > 1 {
                res += (val *(val-1)) *8/2;
            }
        }
        res
    }
}
