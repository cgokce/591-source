/*
Maximum Product of Two Elements in an Array
<T> Array

Given: arr<int> -> nums
    choose different indices i and j of array.
    return max value of (nums[i]-1) * (nums[j]-1)

Fancy description, its just a request for getting two max numbers from an array.
*/


class Solution {
    public int maxProduct(int[] nums) {
       
            
        // Just sort the array
        // Get the multiply of max 2 numbers
        
        Arrays.sort(nums); // should be about O(n) depending on sort
        return (nums[nums.length-1]-1) * (nums[nums.length-2]-1);
        
    }
}