'''
arr: nums
-> a, b elements appear only once
-> others appear only twice

abcc
abccdd
-> Find the a,b!
-> Order or result is not important


Naive Solution: 
-> Use another array that holds the found values, worst time ? should be n^2
-> Also needs hashmamp structure, so this is not feasible
-> Space constraint is also doubled O(n)added space complexity





'''


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        temp_array = []
        #O(n)
        for item in nums:
            if temp_array == []:
                temp_array.append(item)
            else:
                #O(m)
                if item in temp_array:
                    temp_array.remove(item)
                else:
                    temp_array.append(item)
        
        return temp_array
        
        