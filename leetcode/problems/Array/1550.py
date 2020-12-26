'''
Three Consecutive Odds

int [] arr

- Return true if there are three consecutive odd nums in arr



'''
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        
        def isOdd(x):
            return x%2 == True
        
        
        for i in range(len(arr)-2):
            
            if isOdd(arr[i]) and isOdd(arr[i+1]) and isOdd(arr[i+2]):
                return True
            
        return False