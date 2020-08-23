/*

Count Good Triplets
<T> Array

Given: arr:int
       a, b, c
       Find the number of good triplets
       
# Triplet (arr[i], arr[j], arr[k]) is good if:
                 i < j < k 

            arr[j] - arr[i] <=a 
            .. <=b
            .. <=c


Return the number of good triplets


*/

class Solution {
    public int countGoodTriplets(int[] arr, int a, int b, int c) {
  
        
        // We'll just straightforward iterate O(n^3)
        
        int count = 0;
        int n = arr.length;
        int c1, c2, c3;
        
        // First one
        for(int i=0; i<n-2; i++){
            
            // Second one
            for(int j=i+1; j<n-1; j++){
                
                // Third one
                for (int k=j+1; k<n; k++){
                    
                    c1 = Math.abs(arr[i]-arr[j]);
                    c2 = Math.abs(arr[j]-arr[k]);
                    c3 = Math.abs(arr[k]-arr[i]);
                    
                    if (c1 <=a  && c2 <=b && c3 <=c){
                        count++;
                    }
                    
                    
                }
                
            }
            
        }
        
        return count;
        
    }
}