/**
 * @param {number[]} nums
 * @return {number}
 */
var longestSquareStreak = function(nums) {
    const set_nums = new Set(nums);
    let longest = 1;
    for(let x of nums){
        let cur_long = 1;
        while(set_nums.has(x**2)){
            cur_long += 1;
            x *= x;
        }
        longest = Math.max(longest , cur_long);
    }
    return longest > 1 ? longest : -1 ;
    
};
