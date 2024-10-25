/**
 * @param {string[]} folder
 * @return {string[]}
 */
var removeSubfolders = function(folder) {
    folder.sort();
    let res = [];
    let hash = {};
    for(let f of folder){
        let temp = "";
        let bool = true;
        for(let i=0; i<f.length; i++){
            if(f[i] == '/' && temp in hash){
                bool = false;
            }
            temp += f[i];
        }
        if(bool){
            hash[temp] = true;
            res.push(temp);
        }    
    } 
    return res;
};
