/*
Running Sum of 1d Array
<T> Array

Given: arr -> nums

runningSum[i] = sum(nums[0]...nums[i])


This is kind of dp solution, like fibonacci numbers
running[i] = running[i-1] - nums[i]


It can also be in place but I won't bother
so it'll be O(n) time and space

*/


class Solution {
    public int[] runningSum(int[] nums) {
        
        int[] running = new int[nums.length];
        
        running[0] = nums[0];
            
        for(int i=1; i<nums.length; i++){
            
            
            running[i] = running[i-1] + nums[i];
            
        }
        
        return running;
        
    }
}