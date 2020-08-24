/*
Sort Array By Parity
<T> Array

Given: arr A , non negative integers

return: arr, all the even elements of A, followed by all the odd elements of A


*/

import java.util.ArrayList;

class Solution {
    public int[] sortArrayByParity(int[] A) {

        
        int[] res = new int[A.length];
        int t = 0;
        
        for(int i = 0;i<A.length; i++){
            
            if (A[i] %2 == 0) {
                res[t] = (A[i]);
                t++;
            }
            
        }
        for(int i = 0;i<A.length; i++){
            
            if (A[i] %2 == 1) {
                res[t] = (A[i]);
                t++;
            }
            
        }
        
        return res;
        
    }
}