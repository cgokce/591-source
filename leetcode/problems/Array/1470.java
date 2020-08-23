/*
Shuffle the Array
<T> Array

Given: arr<nums>
      2*n elements in form
      x1....xn, y1...yn
      return
      x1y1x2y2....xnyn



a b x y
len 4
4/2 = 2

i->0
x[0 + i] a
x[2 + i ] x
i->1
x[0 + 1] b
x[2 + 1] y


*/

class Solution {
    public int[] shuffle(int[] nums, int n) {
        
        int[] newArray = new int[n*2];
        
        
        for(int i=0; i<n; i++){
            
            newArray[2*i] = nums[i];
            newArray[2*i+1] = nums[n + i];
            
        }
        
        
        return newArray;
    }
}