'''
Defuse the Bomb
<T> Array


int [n] code, circular
int k, key

- to decrypt, replace every number
    - if k>0, replace ith num with sum of next k numbers
    - if k<* replace ith with sum of prev k numbers
    - if k==0, replace ith with 0



'''
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        out =  [0 for i in range(len(code))]
    
        if k == 0:
            return out
        elif k >0:            
            for a in range(len(code)):
                count = k
                total = 0
                i = a
                while (count > 0):
                    if i == len(code) -1:
                        i = 0
                    else:
                        i+= 1
                        
                    total += code[i]
                    
                    count -= 1
                out[a] = total
        elif k<0:
            for a in range(len(code)):
                count = abs(k)
                total = 0
                i = a
                while (count > 0):
                    
                    if i == 0:
                        i = len(code) - 1
                    else:
                        i -= 1
                    total += code[i]
                    
                    count -= 1
                out[a] = total
        
        return out