'''
XOR Operation in an Array
given: integers n and start
- define array nums, nums[i]=start + 2*i
- Return bitwise XOR of all nums

'''


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        
        ### build the xor array
        ret = [start + 2*i for i in range(n)]
        
        #print(ret)
        
        res = ret[0]
        
        ### traverse with xor operation
        for i in range(1,len(ret)):
            res = res ^ ret[i]
        
        return res