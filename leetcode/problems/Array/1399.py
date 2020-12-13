'''
Count Largest Group
<T> Array

int n

- each num 1 to n grouped according to the sum of its digits
    - return the group with the largest size
    

- iterate and use hmap to keep the counts
    - to get the sum of digits, we'll do simple trick ->str->then map to int and sum

'''
class Solution:
    def countLargestGroup(self, n: int) -> int:
        
        hmap = {}    
            
        for i in range(1, n+1, 1):
            item = sum([int(c) for c in str(i)])
            
            if item in hmap:
                hmap[item].append(i)
            else:
                hmap[item] = [i]
                
        
        countMap = {}
        
        for k in hmap.keys():
            #print(k, hmap[k])
            item = len(hmap[k])
            if item in countMap:
                countMap[item] += 1
            else:
                countMap[item] = 1
                
        
        ret = countMap[max(countMap.keys())]
        '''
        for k in countMap.keys():
            ret = max(ret, countMap[k])
        '''
        
        return ret
            
        