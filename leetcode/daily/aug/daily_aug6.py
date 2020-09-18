'''
arr(1,n): int

constraints
--> Some elements(k) appear twice, others appear once.
--> Find k


Challenge:
--> O(n) runtime 
--> Without extra space


Naive Solution
--> HashSet, lookup is O(1), so it'll be O(n) total
--> Problem, it needs total of O(n) space (n-k hmap, k out_array)

Math solution
--> Each num in array corresponds to a valid index(x-1)
--> We traverse once, make the found indices negative(as marking as seen)
--> If we encounter negative(already marked) elem at indexing, we conclude as found dupes


'''



class Solution(object):
    
    ''' This is method 1, needs O(n) memory
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        hset = set()
        duplicates = []
        
        for elem in nums:
            if elem in hset:
                duplicates.append(elem)
            else:
                hset.add(elem)

        return duplicates
    '''
    
    ''' This is better time O(n), memory O(1) '''
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        duplicates = []
        
        for i in range(len(nums)):
            
            elem = nums[i]
            
            #print(nums)
            
            if elem<0:
                elem = elem * -1
                    
            if nums[elem-1] <0:
                duplicates.append(elem)
            else:
                nums[elem-1] *= -1
    

        return duplicates
    
    
        
        
        
        