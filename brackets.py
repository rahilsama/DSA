class Solution:
    def minInsertions(self, s: str) -> int:
        arr = list(s)
        count = 0
        i = 0
        while i < len(arr):
            if arr[i] == ')':
                if i == (len(arr)-1):
                    count +=1
                else:
                    if arr[i+1] == ')':
                        arr.pop(i+1)
                    else:
                        count+=1
            i+=1
        # print(arr) 
        j = 0
        stack = []
        while j < len(arr):
            if arr[j] == '(':
                stack.append(arr[j])
                # if j == (len(arr)-1):
                #     break
                # else:
                #     for k in range(j+1, len(arr)):
                #         if arr[k] == ')':
                #             arr.pop(k)
                #             arr.pop(j)
                #             j-=1
                #             break
            else:
                if stack:
                    stack.pop()
                else:
                    count+=1
            j+=1
                        
        
        if len(stack)!=0:
            for item in stack:
                if item == '(':
                    count+=2
                else:
                    count+=1               
                        
        # print(arr)
        return count
        
        

                    
            
def main():
    solution = Solution()
    
    result = solution.minInsertions("())")
    print("Insertions needed:", result)

if __name__ == "__main__":
    main()