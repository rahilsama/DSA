class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            
            for j in range(i+1, len(nums)):
                point1 = nums[i]
                point2 = nums[j]
                if point2 < point1:
                    nums[i] = point2
                    nums[j] = point1
                
                
                

def sortColors(self, nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            point1 = nums[i]
            point2 = nums[j]
            print(point2)
            if point2 < point1:
                nums[i] = point2
                nums[j] = point1      
            print(nums)  
                
    # print(nums)      
            

nums = [2,0,1]
sortColors(any, nums)