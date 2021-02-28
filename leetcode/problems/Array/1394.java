/*
Find Lucky Integer in an Array
<T> Array

int[] arr

- Lucky integer is integer has a frequency in the array equal to its value
- return lucky integer
    - if multiple, return largest
    - if there is none, return -1
    
    
sol:
- use hmap, there is no way to do it in first iteration
- iterate hmap to catch values

sol2:
- arr_lenght <= 500, can use count array

*/

class Solution {
    public int findLucky(int[] arr) {
        
        HashMap<Integer, Integer> hmap = new HashMap<>();
        
        for(int item: arr){
            
            if (hmap.containsKey(item)){
                
                int current = hmap.get(item);
                current += 1;
                hmap.replace(item, current);
                
                
            }else{        
                hmap.put(item, 1);                
            }
            
        }
        
        int max = -1;
        
        for(int key: hmap.keySet()){
            int val = hmap.get(key);
            if (key == val){
                max = key;
            }
        } 
        
        return max;
    }
}