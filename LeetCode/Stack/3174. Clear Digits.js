/**
 * @param {string} s
 * @return {string}
 */
var clearDigits = function(s) {
    let stack = [];
    for (let char of s){
        if(/[0-9]/.test(char)){
            stack.pop();
        } else {
            stack.push(char);
        }
    }
    return stack.join('');
};
