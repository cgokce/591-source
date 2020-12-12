'''
Merge Sorted Array
<T> Array

int [m] nums1
int [n] nums2

- merge nums2 into nums1
    - as one sorted array

- Assume
    - nums1 has enough space to hold additional items from num2

- Using very simple trick
    - Since nums1 have extra size at tail with length of nums2
    - Merge them first, then simply sort

'''
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        if not nums2:
            return nums1
        
        if len(nums1) == len(nums2):
            for i in range(len(nums2)):
                nums1[i] = nums2[i]
            return nums1
        
        j = 0
        for i in range(len(nums1) - len(nums2), len(nums1), 1):
            #print(i)
            nums1[i] = nums2[j]
            j += 1
            
        nums1.sort()
        
        return nums1