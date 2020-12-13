'''
Reshape the Matrix
<T> Array

int [][] mat
int r
int c

- r, c is the desired row column for desired matrix
    - fill the final matrix with row trawersing
- if possible, output reshaped
    - else return the original

'''

class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        if r*c != len(nums) * len(nums[0]):
            return nums
        
        flatten = []
        for row in nums:
            for item in row:
                flatten.append(item)
        
        curr = 0
        ret = []
        for i in range(r):
            mid = []
            for j in range(c):
                mid.append(flatten[curr])
                curr += 1
                               
            ret.append(mid)
        return ret               