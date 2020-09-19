'''
Sequential Digits
<T> Backtracking

Values are precalculatable
better we can use pointers to an already sorted string

'''

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s = '123456789'
        
        min_length = len(str(low))
        max_length = len(str(high))
        ret = []
        
        for l in range(min_length, max_length+1):
            for i in range(len(s)):
                
                
                if (i+l)>len(s):
                    break
                
                item = int(s[i:i+l])
                #print("i: ", str(i) ," - l: ", str(l) , " - item: " + str(item))
                
                if item >= low:
                    if (item <= high):
                        ret.append(item)
                    else:
                        break
                
        return ret
