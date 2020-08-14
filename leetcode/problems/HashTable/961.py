'''
N-Repeated Element in Size 2N Array
<T> HashTable

Arr size 2N
    -> N+1 unique elems
    -> 1 element repeated N times


1,2,3,3
N = 2
3 unique elements
N repeated 3 ttimes


Algorithm
- Have a hashset
- Return when you see another occurance

'''


class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        hset = set()
        
        for item in A:
            if item in hset:
                return item
            else:
                hset.add(item)