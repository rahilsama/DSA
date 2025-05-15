#4. Median of two sorted array


# First i have to combine the arrays
# second, i have to sort it 
# Third have to find median and return it

# all of this to be done with complexity of O(log(m+n)) in worst case

#Divide and conquer strat


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float: