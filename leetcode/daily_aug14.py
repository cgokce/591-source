'''
Longest Palindrome
<T> String, <T> HashMap

Obj
Generate the longest palindrome
- Every double char included in the palindrome
- Only one single char included in the palindrome

Algorithm:
hset[i] = None
total_count = 0

# Count double.
for item in s:
    if s in hashmap[i]:
        total_count += 1
        hashmap.remove(s)

'''


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        hset = set()
        count = 0
        
        for item in s:
            if item in hset:
                count += 1
                hset.remove(item)
            else:
                hset.add(item)
                
        if (2*count) < len(s):
            return 2*count + 1
        return 2*count
        
        
        
        
        