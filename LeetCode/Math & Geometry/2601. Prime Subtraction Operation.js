/**
 * @param {number[]} nums
 * @return {boolean}
 */
var primeSubOperation = function(nums) {
    function check_prime(num){
        if(num <= 1){
            return false;
        }
        if(num === 2){
            return true;
        }
        for(let i = 2 ; i < Math.floor(Math.sqrt(num)) +1 ; i++){
            if(num % i === 0){
                return false;
            }

        }
        return true;
    }
    let prime_arr = [false , false];
    let max_num = nums[0];
    for(let i = 1 ; i < nums.length ; i++){
        if(nums[i] > max_num){
            max_num = nums[i];
        }
    }
    for(let x = 2 ; x < max_num ; x++){
        if(check_prime(x)){
            prime_arr.push(true);
        }else {
            prime_arr.push(false);
        }
    }
    let prev_val = 0;
    for(let num of nums){
        let biggest_prime = 0;
        for(let x = num - prev_val - 1 ; x > 2 - 1 ; x--){
            if(prime_arr[x] === true){
                biggest_prime = x;
                break;
            }
        }
        if(num - biggest_prime <= prev_val){
            return false;
        }
        prev_val = num - biggest_prime;
    }
    return true;
};
