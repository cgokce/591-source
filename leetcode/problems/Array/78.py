'''
Easier solution would be collections combinations
keep results in a hashset to avoid dupes
wow. easy


'''

from itertools import combinations

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        
        for i in range(1, len(nums)+1):
            res.extend(combinations(nums, i))
        
        # Conversion here because of hash function gives an error for the empty list (not hashable)
        res = list(set(res))
        res.append([])
        
        return res