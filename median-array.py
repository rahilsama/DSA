#4. Median of two sorted array


# First i have to combine the arrays
# second, i have to sort it 
# Third have to find median and return it

# all of this to be done with complexity of O(log(m+n)) in worst case

#Divide and conquer strat

from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        #Combine the array
        combinedArray = nums1 + nums2
        print(combinedArray)
        
        p=0
        q=1
        r=2
        
        sort = merge(combinedArray, p, q, r)
        print(sort)
        
        


def merge(A: List[int], p:int, q:int, r:int) -> List[int]:
    n1 = q-p+1
    n2 = r-q
    
    lArr = []
    rArr = []
    
    for i in range(n1):
        lArr.append(A[p+i])
    print(lArr)
    for j in range(n2):
        rArr.append(A[q+j+1])
    print(rArr)
    i=0
    j=0
    for k in range(p,r+1):
        if i >= len(lArr):
            A[k] = rArr[j]
            j+=1
        elif j >= len(rArr):
            A[k] = lArr[i]
            i+=1
        else:
            if lArr[i]<=rArr[j]:
                A[k] = lArr[i]
                i+=1
            else:
                A[k] = rArr[j]
                j+=1
        
    return A    
    
    




if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 3]
    nums2 = [2]
    median = solution.findMedianSortedArrays(nums1, nums2)
    print("The median is:", median)