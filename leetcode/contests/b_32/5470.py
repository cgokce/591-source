'''
str: s -> input string
return int

obj:
-> Find if the tree is balanced

algo:
simple traversal
for 1 "(" we need 2*")"


# Another solution
# Dfs, at every node we have 3 choices:
# Add (, add ), do nothing
# Problem =-> add options goes to infinite


# More valid solution
# For every ))
# we need to handle it by inserting ( before

Traverse from beginning

inserted = 0
    if i == ")":
        r += 1
        if r == 2:
            # Need balance
            if l==0:
                inserted += 1
            else:
                l-=1




'''


class Solution:
    '''
    def minInsertions(self, s: str) -> int:
        l = 0
        r = 0
        
        for i in s:
            if i == "(":
                l+=1
            else:
                r+=1
        
        print(l,r)
        # Naive output
        print(abs(2*l - r))
    '''
    '''
    def minInsertions(self, s: str) -> int:
        l = 0
        r = 0
        inserted = 0
        
        print("---------")
        
        # Balance rights
        for i in s:
            if i == ")":
                print("r")
                r += 1
                if r == 2:
                    # Need balance
                    if l==0:
                        inserted += 1
                    else:
                        l-=1
            else:
                print("l")
                l += 1
        
        print(l,r,inserted)
        # If leftover rights
        if r == 1:
            if l>0:
                inserted += 1
                l-=1
            else:
                inserted += 2
                
        print(l,r,inserted)
        # If leftover lefts
        if l<0:
            inserted += l
        else:
            inserted += l*2
        
        print(l,r,inserted)
            
        
        return inserted
      '''  
        
    # 4. hold an helper arr
    # for each left
    # insert 2
    # it'll decrease with right
    def minInsertions(self, s: str) -> int:
        print("-----")
        q = collections.deque()
        inserted = 0 
        prev_right = False
        #print("Start: ", str(q))
        
        for i in s:
            if i == "(":
                if prev_right:
                    # close all prev q's
                    for i in q:
                        inserted += i

                    q = collections.deque()
                    prev_right = False
                q.append(2)
            else:
                if q == collections.deque():
                    q.append(1)
                    inserted += 1
                else:
                    q[-1] -= 1
                    if q[-1] == 0:
                        q.pop()
                    prev_right = True
                            

            #print(i , " -> ", str(q))

        #print("Final: ", str(q), " ", inserted)
        for i in q:
            if i:
                inserted += i
        return inserted
                    
#"(()))(()))()())))"        
# Out:1
# Exp:4


#"(((()(()((())))(((()())))()())))(((()(()()((()()))"
# Out:40
# Exp:31