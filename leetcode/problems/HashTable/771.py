'''
Jewels and Stones
<T> HashTable


All chars alphabetical, and case sensitive

J -> Jewels
S -> Stones -> each character is the type of stones
    -> Want to know how many stones are also jewels
    
char in J all unique
n<50


Algorithm:
Put J in hash set
traverse S check if item in set

Time: O(len(j) + len(s)) --> O(n)
Memory: Hashmap for j, so O(len(j))
'''


class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        
        hset = set()
        
        for item in J:
            hset.add(item)
        
        count = 0
        for item in S:
            if item in J:
                count += 1
        
        return count
        