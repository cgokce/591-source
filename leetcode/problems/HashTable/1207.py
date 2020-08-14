'''
Unique Number of Occurences
<T> HashTable

Given: arr<int> arr
--> Return true if each value of occurance is unique

we can store counts using the hmap
'''

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        # Hmap for calculating the counts
        hmap = {}
        
        for item in arr:
            if item in hmap:
                hmap[item] += 1
            else:
                hmap[item] = 1
         
        print(hmap)
        #  hset to find duplicates in counts
        hset = set()
        
        for i,k in enumerate(hmap):
            item = hmap[k]
            if item in hset:
                return False
            else:
                hset.add(item)
                
        print(hset)
        return True