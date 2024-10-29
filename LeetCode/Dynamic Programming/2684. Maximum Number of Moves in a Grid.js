/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxMoves = function(grid) {
  
    let dp = {};
    function dfs(r , c){
        const key = `${r},${c}`;
        if(key in dp){
            return dp[key];
        }
        let move = 0;
        const positions = [[r - 1, c + 1], [r, c + 1], [r + 1, c + 1]];
        for (const [x , y] of positions){
            if((0<= x && x<grid.length) && (0<= y && y<grid[0].length) && (grid[x][y] > grid[r][c])){
                move = Math.max(move, 1 + dfs(x, y));
            }
        }
        dp[key] = move;
        return dp[key];
    }
    let max_moves = 0;
    for(let row = 0 ; row < grid.length ; row++){
        max_moves = Math.max(max_moves , dfs(row , 0));
    }
    return max_moves;

};
