class Solution {
    public long minimumSteps(String s) {
        long res = 0;
        int right = s.length() - 1;
        for(int left = s.length() - 1 ; left >= 0 ; left--){
            if(s.charAt(left) == '1'){
                res += right - left;
                right-- ;
            }
        }
        return res;
    }
}
