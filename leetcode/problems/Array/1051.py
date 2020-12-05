'''
Height Checker
<T> Array

Students stand in increasing order heights
- Return minimum number must move to sorted increasing


Brute force ish
heights 
goal

- We wil sort, then simple count O(nlogn)


'''

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        goal = sorted(heights)
        
        ret = 0
        for i in range(len(heights)):
            if goal[i] != heights[i]:
                ret += 1
        
        return ret