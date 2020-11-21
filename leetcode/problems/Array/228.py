'''
Summary Ranges
<T> Array

Since array is sorted
O(n) solution we will just iterate while calculating current array

'''

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        ret = []
        seq_start = None
        count = 0
        
        for i in range(len(nums)):
            
            
            item = nums[i]
            count += 1
            
            if seq_start == None:
                seq_start = item
            
            ## Final char
            if i == len(nums) -1:
                if count == 1:
                    ret.append(str(item))
                else:
                    ret.append(str(seq_start) + "->" + str(item))
                count = 0
                seq_start = None
                continue
            

            next_item = nums[i+1]


            ## Terminal condition
            if next_item != item+1:

                if count == 1:
                    ret.append(str(item))
                else:
                    ret.append(str(seq_start) + "->" + str(item))
                count = 0
                seq_start = None

        return ret