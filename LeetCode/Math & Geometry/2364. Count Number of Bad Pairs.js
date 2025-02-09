/**
 * @param {number[]} nums
 * @return {number}
 */
var countBadPairs = function(nums) {
    const n = nums.length ;
    const d = new Map() ; 
    for (let i = 0 ; i < n ; i++) {
        let key = i - nums[i];
        d.set(key , (d.get(key) || 0) + 1);
    }
    let total = n*(n - 1)/2;
    let good_pairs = 0;
    for (let count of d.values()) {
        good_pairs += (count*(count-1) / 2);
    }
    return total - good_pairs; 
};
