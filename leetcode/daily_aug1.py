'''
Aug#1 Daily - Detect Capital


Constraints
given string s
Capital True if
 --> All letters Uppercase
 --> First letter only uppercase
 
Usage true if
  --> All in lower_case
Otherwise false
 
Algorithm
def algo(s):


    # Check if len(s) is 1
    if len(s) == 1:
        return 1


    first_char = s[0]
    first_uppercase = check_uppercase(first_char)
    
    if first_uppercase:
        
        all_up = True
        all_down = True
        
        for char in s[1:]:
            curr_up = checkuppercase(char)    
    
            if curr_up:
                all_down= False
            else
                all_up = False
                
        if all_up or all_down:
            # Success condition
            return true
    
    else:
    
        all_up = True
        all_down = True
        
        for char in s[1:]:
            curr_up = checkuppercase(char)    
    
            if curr_up:
                all_down= False
            else
                all_up = False
        
        if all_down:
            # Success condition
            return True
    
    
    # Failure Condition
    return False


def check_uppercase(char):
    if char is uppercase:
        return True
    else:
        return False


Istanbul
-> first char = True
-> all_down = True
----> Return True

ISTANBUL
-> first char = True
-> all_up = True
----> Return True

IsTanBul
-> first char = True
-> all_up, all_down = False
----> Return False

istanbul 
-> first char = False
----> Return False

-> 



'''




class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        # Check if len(s) is 1
        if len(word) == 1:
            return 1
        
        first_char = word[0]
        first_uppercase = first_char.isupper()
        
        print(word[0])
        print(first_uppercase)
        
        
        if first_uppercase:

            all_up = True
            all_down = True

            for char in word[1:]:
                curr_up = char.isupper()    

                if curr_up:
                    all_down= False
                else:
                    all_up = False

            if all_up or all_down:
                # Success condition
                return True
            
        else:
    
            all_up = True
            all_down = True

            for char in word[1:]:
                curr_up = char.isupper()

                if curr_up:
                    all_down= False
                else:
                    all_up = False

            if all_down:
                # Success condition
                return True
    

        # Failure Condition
        return False
        
    
    # There is a built in function for uppercase testing, we will use it
    #.isupper()
