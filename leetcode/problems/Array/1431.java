/*

Kids With the Greatest Number of Candies
<T> Array


Given: arr -> candies
       int -> extraCandies
       
- candies[i] represents number of candies ith kid has

return i = true if arr[i]+extraCandies be max of the array 


O(n) find max value
O(n) check if current is max

result O(n) time O(n) space(bool array)


*/


class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        
        int max = 0;
        List<Boolean> res = new ArrayList<>();
        
        // find max
        for (int i =0; i< candies.length; i++){
            if (candies[i] >= max){
                max = candies[i];
            }    
        }
        
        // get result
        for (int i=0; i<candies.length; i++){
            
            if (candies[i] + extraCandies>=max){
                res.add(true);
            }else{
                res.add(false);
            }
                
        }
        return res;
        
        
    }
}