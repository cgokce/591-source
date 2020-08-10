'''
str:s --> lower&upper case english letters

good string
doesnt have
- s[i] and s[i+1] adjacent
- 0<=i<=s.length-2
s[i] lowercase i+1 uppercase
s[i] uppercase i+1 lowercase

-> Remove all adjacents, return it
-> Empty string is also good
'''


class Solution:
    def makeGood(self, s: str) -> str:
              
        found_flag = True
        
        while(found_flag):
            found_flag = False
            out_str = ""
            print("--- ", s ," ---")

            if len(s)<=1:
                return s 
            
            i = 0
            while i<len(s)-1:
                
                a = s[i]
                b = s[i+1]

                print(a,b)
                
                if a != b and a.upper() == b:
                    print("cut")
                    found_flag = True
                    i = i+2
                    if i == len(s)-1:
                        out_str += s[i]
                elif a != b and a.lower() == b:
                    print("cut")
                    found_flag = True
                    i = i+2
                    if i == len(s)-1:
                        out_str += s[i]
                else:
                    out_str += a
                    i = i+1
                    if i == len(s)-1:
                        out_str += b
                 

            


            s = out_str
        
        return s
            
            