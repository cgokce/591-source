'''
Check if two string arrays are equivalent
<T> String

- string [] word1
- string [] word2

- return true if the two arrays represent the same string
- meaning that those should result in same string when concatenated


'''

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        out_w1 = ""
        out_w2 = ""
        
        for item in word1:
            out_w1 += item
            
        for item in word2:
            out_w2 += item
            
        return out_w1 == out_w2
        
        