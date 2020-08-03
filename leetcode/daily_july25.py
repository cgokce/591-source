
'''
arr: input, sorted ascending

const
rotated at some piveot unkown (k)
eg(3:)

0,1,2 --- k --- 4,5,6,7

4,5,6,7 --- 0,1,2

result is on k+1

--> can contain duplicates


naive brute force algorithm
Straight O(n) complexity
Dupes increase the cost linearly

take current, next
iterate until end
    if next<curr
        break

return next


Better is the  randomized approach, like quicksort
take two random spots, a(range(1,len)) b(range(a,len))
recursive

if a < b
    recurse(b:)
if a > b
    recurse(a:b)

end case 

4,5,6,7 --- 0,1,2
5, 1
a>b
recurse
5,6,7 --- 0,1
6,0
recurse
6,7 --- 0
better selection, this should take either 6,7 or 7,0
6,7 a<b return 7:0, size 2 --> exit
7,0

End case randomness should be strictly tailored
Maybe later
This should average O(1)


'''

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #nums = [3,1]
        found = False
        
        if len(nums) == 1:
            return nums[0]
        
        # O(n) solution
        for i in range(1,len(nums)):
            if nums[i]< nums[i-1]:
                found = True
                break
    
        if found:
            return nums[i]
        else:
            # Not inverted arrays
            return nums[0]
    