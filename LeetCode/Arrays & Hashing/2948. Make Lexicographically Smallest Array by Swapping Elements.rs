// You are given a 0-indexed array of positive integers nums and a positive integer limit.
// In one operation, you can choose any two indices i and j and swap nums[i] and nums[j] if |nums[i] - nums[j]| <= limit.
// Return the lexicographically smallest array that can be obtained by performing the operation any number of times.
// An array a is lexicographically smaller than an array b if in the first position where a and b differ, array a has an element that is less than 
// the corresponding element in b. For example, the array [2,10,3] is lexicographically smaller than the array [10,2,3] because they differ at index 0 and 2 < 10.

// Example 1:
// Input: nums = [1,5,3,9,8], limit = 2
// Output: [1,3,5,8,9]
// Explanation: Apply the operation 2 times:
// - Swap nums[1] with nums[2]. The array becomes [1,3,5,9,8]
// - Swap nums[3] with nums[4]. The array becomes [1,3,5,8,9]
// We cannot obtain a lexicographically smaller array by applying any more operations. Note that it may be possible to get the same result by doing different operations.
  
// Example 2:
// Input: nums = [1,7,6,18,2,1], limit = 3
// Output: [1,6,7,18,1,2]
// Explanation: Apply the operation 3 times:
// - Swap nums[1] with nums[2]. The array becomes [1,6,7,18,2,1]
// - Swap nums[0] with nums[4]. The array becomes [2,6,7,18,1,1]
// - Swap nums[0] with nums[5]. The array becomes [1,6,7,18,1,2] 
// We cannot obtain a lexicographically smaller array by applying any more operations.

// Constraints:
// 1 <= nums.length <= 10**5
// 1 <= nums[i] <= 10**9
// 1 <= limit <= 10**9

use std::collections::{HashMap, VecDeque};
impl Solution {
    pub fn lexicographically_smallest_array(nums: Vec<i32>, limit: i32) -> Vec<i32> {
        let mut nums_sorted = nums.clone();
        nums_sorted.sort();
        let mut groups: Vec<VecDeque<i32>> = Vec::new();
        let mut d: HashMap<i32, usize> = HashMap::new();
        for &num in &nums_sorted {
            let mut should_create_new_group = true ;
            if let Some(last_group) = groups.last(){
                if let Some(&last_num) = last_group.back(){
                    if(num - last_num).abs() <= limit {
                        should_create_new_group = false ;
                    }
                }
            }
            if should_create_new_group {
                groups.push(VecDeque::new());
            }
            if let Some(last_group) = groups.last_mut() {
                last_group.push_back(num)
            }
            d.insert(num, groups.len() - 1);
        }
        let mut res = Vec::new();
        for &num in &nums {
            if let Some(&group_idx) = d.get(&num){
                if let Some(val) = groups[group_idx].pop_front(){
                    res.push(val);
                }
            }
        }
        res
    }
}
