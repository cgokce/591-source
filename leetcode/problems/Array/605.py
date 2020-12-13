'''
Can Place Flowers
<T> Array


int [] flowerbed

- flowers cannot be planted in adjacent plots
    - 0 = empty
    - 1 = full

int n
    - return if n new flowers can be planted in the flowerbed without violation

'''

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        if n == 0:
            return True
        
        count = 0
        for i in range(len(flowerbed)):
            
            if flowerbed[i] == 0:
                if i == 0:
                    left = 0
                else:
                    left = flowerbed[i-1]


                if i == (len(flowerbed) -1):
                    right = 0
                else:
                    right = flowerbed[i+1]

                if left == 0 and right == 0:
                    print(i)
                    count += 1
                    flowerbed[i] = 1
                    if count >=n:
                        return True
                
        return False
        
        