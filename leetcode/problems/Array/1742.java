/*
Maximum Number of Balls in a Box
<T> Array

- N balls numbered [lowlimit, higjlimit]
- Infinite number of boxes [1, infinity]

Constraints:
- Job at factory put each ball in the box with a number equal to the sum of digits of ball's number
- Eg. ball 321 put in 3+2+1 = 6 , 10 will 1+0=1
- Return the number of balls in box with most balls

Sol:
- As a box keep a hashmap and count
- To get digits, convert to string then int


*/

class Solution {
    
    public int sumDigits(int num){
        
        int sum = 0;
        int lastDigit = 0;
        
        while(num != 0){
            lastDigit = num % 10;
            sum = sum + lastDigit;
            num = num/10;
        }
        return sum;
        
    }
    
    public int countBalls(int lowLimit, int highLimit) {
        
        HashMap<Integer, Integer> hmap = new HashMap<>();
        int max = 0;
        int item;
        
        for(int i = lowLimit; i <= highLimit; i++){
            // System.out.println("DigitSum: " + sumDigits(item));
            item = sumDigits(i);
            
            if (hmap.containsKey(item)){
                int current = hmap.get(item);
                current += 1;
                if (current > max){
                    max = current;
                }
                hmap.replace(item, current);
                
            }else{
                hmap.put(item, 1);
                if (max == 0){
                    max = 1;
                }
            }
            
        }
        
        return max;
        
    }
}