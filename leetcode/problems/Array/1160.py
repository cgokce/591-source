'''
Find Words That Can Be Formed By Characters
<T> Array

String [] words
String chars

- String is good if it can be formed by characters from chars
    - Each char used once
- Return the sum of lengths of all good strings in words

'''

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        hmap = {}
        
        for c in chars:
            
            if c in hmap:
                hmap[c] += 1 
            else:
                hmap[c] = 1
            
        
        ret = 0
        
        for w in words:
            
            ## Check valid
            new_map = hmap.copy()
            valid = True
            
            for c in w:
                
                if (c in new_map) and new_map[c]>0:
                    new_map[c] -= 1
                else:
                    valid = False
                    break
            
            if valid:
                ret += len(w)
        
        return ret
                    
            