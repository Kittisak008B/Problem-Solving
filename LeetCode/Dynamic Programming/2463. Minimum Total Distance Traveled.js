/**
 * @param {number[]} robot
 * @param {number[][]} factory
 * @return {number}
 */
var minimumTotalDistance = function(robot, factory) {
    let dp = {};
    function dfs(bot , fac , limit){
        const key = `${bot},${fac},${limit}`;
        if(bot >= robot.length){
            return 0;
        }
        if(fac >= factory.length){
            return Infinity;
        }
        if(key in dp){      
            return dp[key];
        }
        let skip_repair = dfs(bot , fac + 1 , 0);
        let repair = Infinity;
        if(factory[fac][1] > limit){
            const distance = Math.abs(factory[fac][0] - robot[bot]);
            repair = distance + dfs(bot + 1 , fac , limit + 1);
        } 
        dp[key] = Math.min(skip_repair , repair);
        return dp[key];
    }
    robot.sort((a , b)=> a - b);
    factory.sort((a , b)=> a[0] - b[0]);
    return dfs(0 , 0 , 0);
    
};
