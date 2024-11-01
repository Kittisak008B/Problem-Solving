// A fancy string is a string where no three consecutive characters are equal. 
// Given a string s, delete the minimum possible number of characters from s to make it fancy.
// Return the final string after the deletion. It can be shown that the answer will always be unique.

// Example 1:
// Input: s = "leeetcode"
// Output: "leetcode"
// Explanation:
// Remove an 'e' from the first group of 'e's to create "leetcode".
// No three consecutive characters are equal, so return "leetcode".

// Constraints:
// 1 <= s.length <= 10**5
// s consists only of lowercase English letters.

/**
 * @param {string} s
 * @return {string}
 */
var makeFancyString = function(s) {
    let res = [];
    res.push(s[0]);
    let count = 1;
    for(let i = 1; i < s.length ; i++){
        if(s[i] === s[i-1]){
            count++;
            if(count < 3){
                res.push(s[i]);
            }
        }
        else{
            count = 1;
            res.push(s[i]);
        }
    }
    return res.join('');
};
