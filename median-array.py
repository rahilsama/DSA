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
        
        p = 0
        r = len(combinedArray)-1
        
        
        mergeSort(combinedArray, p, r)
        print(combinedArray)
        if len(combinedArray)%2==0:
            x = r//2
            median = (combinedArray[x]+combinedArray[x+1])/2
            return median
        
        else:
            median = combinedArray[r//2]
            return median
        
        
        

def mergeSort(arr: List[int], p, r):
    # if len(arr) == 1:
    #     return arr
    # else:
    #     p = 0
    #     q = len(arr)//2
    #     r = len(arr)-1
    #     arr = merge(arr, p, q, r)
    # print("Length if arr: ",len(arr))
    # return mergeSort(arr)
    if p < r:
        q = (p+r)//2
        mergeSort(arr, p, q)
        mergeSort(arr, q+1, r)
        merge(arr, p, q, r)
        
    


def merge(arr: List[int], p:int, q:int, r:int):
    n1 = q-p+1
    n2 = r-q
    
    lArr = []
    rArr = []
    
    for i in range(n1):
        lArr.append(arr[p+i])
    print(lArr)
    for j in range(n2):
        rArr.append(arr[q+j+1])
    print(rArr)
    i=0
    j=0
    for k in range(p,r+1):
        if i >= len(lArr):
            arr[k] = rArr[j]
            j+=1
        elif j >= len(rArr):
            arr[k] = lArr[i]
            i+=1
        else:
            if lArr[i]<=rArr[j]:
                arr[k] = lArr[i]
                i+=1
            else:
                arr[k] = rArr[j]
                j+=1
        
    
    




# if __name__ == "__main__":
#     solution = Solution()
#     nums1 = [1, 3]
#     nums2 = [4, 2]
#     median = solution.findMedianSortedArrays(nums1, nums2)
#     print("The median is:", median)