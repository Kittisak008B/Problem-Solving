// You are given two integers n and x. You have to construct an array of positive integers nums of size n where for every 0 <= i < n - 1, 
// nums[i + 1] is greater than nums[i], and the result of the bitwise AND operation between all elements of nums is x. Return the minimum possible value of nums[n - 1].

// Example 1:
// Input: n = 3, x = 4
// Output: 6
// Explanation:
// nums can be [4,5,6] and its last element is 6.

// Example 2:
// Input: n = 2, x = 7
// Output: 15
// Explanation:
// nums can be [7,15] and its last element is 15.

// Constraints:
// 1 <= n, x <= 10**8

/**
 * @param {number} n
 * @param {number} x
 * @return {number}
 */
// var minEnd = function(n, x) {
//     x = BigInt(x);
//     n = BigInt(n);
//     let res = x ;
//     let remain = n - 1n;
//     while (remain > 0n){
//         res += 1n;
//         res |= x;
//         remain -= 1n;
//     }
//     return Number(res);
// };

var minEnd = function(n, x) {
    x = BigInt(x);
    n = BigInt(n);
    let res = x;
    let remain = n - 1n;
    let pos = 1n;
    while (remain > 0n){
        if((x & pos)=== 0n){
            res |= pos*(remain & 1n);
            remain >>= 1n;
        }
        pos <<= 1n;
    }
    return Number(res);
};
/**
n = 3, x = 4 -> 100(binary)
                remain=10 res = 100  pos=1   pos*(remain & 1n) = 0  res=100
                remain=1  res = 100  pos=10  pos*(remain & 1n) = 10 res=110
                remain=0
*/
