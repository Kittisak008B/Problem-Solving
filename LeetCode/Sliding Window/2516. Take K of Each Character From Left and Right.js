/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var takeCharacters = function(s, k) {
    const freq = {};
    for (const c of s){
        freq[c] = (freq[c] || 0) + 1;
    }
    if ((freq['a'] || 0) < k || (freq['b'] || 0) < k || (freq['c'] || 0) < k){
        return -1;
    }
    let res = s.length;
    let left = 0;
    for (let right = 0; right < s.length; right++){
        freq[s[right]]--;
        while (freq[s[right]] < k){
            freq[s[left]]++;
            left++;
        }
        res = Math.min(res, s.length - (right - left + 1));
    }
    return res;
};
