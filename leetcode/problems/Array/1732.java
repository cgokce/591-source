/*
Find the Highest Altitude
<T> Array

int[n] gain
    - gain[i] is the net gain in altitude between i and i+1
    - Return the highest altitude of a point

Constraints:
- Biker is going to a road trip
- n+1 different altitudes
- Starts trip on point 0 with altitude 0

Sol:
- Starting from alt 0
- Adding through the points
- Return the max val, find max sum until arr[i]


*/

class Solution {
    public int largestAltitude(int[] gain) {
        
        int sum = 0;
        int max = 0;
        int maxInd = 0;
        
        for(int i = 0; i < gain.length; i++){
            
            sum += gain[i];
            //System.out.println("Sum: " + sum + "   Max: " + max);
            
            if (sum > max){
                max = sum;
            }
        }
        
        return max;
        
    }
}