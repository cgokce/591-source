/*

int[] nums

Return sum of all unique elements

Sol:
- Keep a hashset
- If elem is not in hashset add to sum
- If elem is in hashset remove from sum
- Does not satisfy multiple items

Sol2:
- Keep a hashmap with count
- If elem is not in hmap set 1, add to sum
- If is in hmap increment val
    - If val==1 remove from sum

*/

class Solution {
    public int sumOfUnique(int[] nums) {
        
        // Sol2
        HashMap<Integer, Integer> hmap = new HashMap<>();
        int sum = 0;
        
        for(int item:nums){
            
            if (hmap.containsKey(item)){
                
                // Get value, if 1 minus sum
                int currVal = hmap.get(item);
                if (currVal == 1){
                    sum -= item;   
                }
                
                hmap.replace(item, currVal + 1);
                
            }else{
                // Add <k, 1> to hmap
                hmap.put(item, 1);
                sum += item;
            }
        }
        
        return sum;
        
        /*
        // Sol1: Does not work with duplicates more than 3
        
        HashSet<Integer> set = new HashSet<Integer>();
        int sum = 0;
        
        for(int item:nums){
            //System.out.println(item);
            if (set.contains(item)){
                sum -= item;        
            }else{
                set.add(item);
                sum += item;
            }
        }
        
        return sum;
        */
        
    }
}