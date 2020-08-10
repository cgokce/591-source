'''
arr:int[] --> all positive, sorted increasing order
k:int

Obj
---> Find the kth positive integer missing from array.




# Greedy

current_val = 1
missing_arr = []

for item in arr:
    while current_val < item:
        current_val += 1
        missing_arr.append(current_val)
        
        if len(missing_arr) == k
            return missing_arr[k-1]
    
    






'''


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        #print("-------------")
        current_val = 1
        missing_arr = []

        for item in arr:
            while current_val < item:
                #print(missing_arr)
                missing_arr.append(current_val)
                #print(current_val,item, str(missing_arr))

                if len(missing_arr) == k:
                    return missing_arr[k-1]
                
                current_val += 1
            current_val += 1
            
        item = arr[-1]+1
        while 1:
                
            missing_arr.append(item)
            #print(item, str(missing_arr))
            #print(missing_arr)

            if len(missing_arr) == k:
                return missing_arr[k-1]
            
            item = item +1

#1313