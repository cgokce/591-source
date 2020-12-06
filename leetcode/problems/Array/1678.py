'''
Goal Parser Interpretation
<T> Array

- Parse string n
        - G -> G
        - () -> o
        - al -> al
        
Given string, parse it according to reqs and return



'''

class Solution:
    def interpret(self, command: str) -> str:
        
        ret = ""
        
        
        i=0
        while i<len(command):
            c = command[i]
            
            if c == "(":
            
                if command[i+1] == "a":
                    ret += "al"
                    i += 4
                elif command[i+1] == ")":
                    ret += "o"
                    i += 2
            
            else:
                ret += c
                i+=1
                
        return ret
            
                    
                
            