// Given an integer array arr, remove a subarray (can be empty) from arr such that the remaining elements in arr are non-decreasing.
// Return the length of the shortest subarray to remove. A subarray is a contiguous subsequence of the array.
  
// Example 1:
// Input: arr = [1,2,3,10,4,2,3,5]
// Output: 3
// Explanation: The shortest subarray we can remove is [10,4,2] of length 3. The remaining elements after that will be [1,2,3,3,5] which are sorted.
// Another correct solution is to remove the subarray [3,10,4].
  
// Example 2:
// Input: arr = [5,4,3,2,1]
// Output: 4
// Explanation: Since the array is strictly decreasing, we can only keep a single element.
// Therefore we need to remove a subarray of length 4, either [5,4,3,2] or [4,3,2,1].
  
// Example 3:
// Input: arr = [1,2,3]
// Output: 0
// Explanation: The array is already non-decreasing. We do not need to remove any elements.
 
// Constraints:
// 1 <= arr.length <= 10**5
// 0 <= arr[i] <= 10**9

/**
 * @param {number[]} arr
 * @return {number}
 */
var findLengthOfShortestSubarray = function(arr) {
    let r = arr.length - 1;
    // Remove the decreasing prefix from the end
    while (r > 0 && arr[r] >= arr[r - 1]){
        r -= 1;
    }
    let res = r;

    let l = 0;
    // Remove the increasing postfix from the start
    while (l + 1 < arr.length && arr[l] <= arr[l + 1]){
        l += 1;
    }
    res = Math.min(res, arr.length - 1 - l);
  
    l = 0;
    r = arr.length - 1;
    // Remove subarray from the middle
    while (l < r){
        while (r < arr.length && l + 1 < r && arr[r - 1] <= arr[r] && arr[l] <= arr[r]){
            r -= 1;
        }
        while (r < arr.length && arr[l] > arr[r]){
            r += 1;
        }
        res = Math.min(res, r - l - 1);
        if (arr[l] > arr[l + 1]){
            break;
        }
        l += 1;
    }
    return res;
};
