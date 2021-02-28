/*
Mean of Array After Removing Some Elements
<T> Array

int[] arr
- remove smallest %5, largest %5
- Answers within 10^-5 range of actual answer will be accepted
- either tricky question or a math question
- arr length is multiply of 20, so there is always %5 min and max

Sol:
- simplest is just sorting
- First %5 is min, last %5 is max, do not use them, calculate mean of the rest

*/

import java.util.Arrays;

class Solution {
    public double trimMean(int[] arr) {
        
        // Sort
        Arrays.sort(arr);
        
        // Calculate %5
        int exclude = arr.length / 20;
        
        int sum = 0;
        System.out.println(exclude + "-" + (arr.length - exclude));
        for(int i = exclude; i < arr.length - exclude; i++ ){
            sum += arr[i];
        }
        
        return sum / (arr.length * 0.9);
        
    }
}