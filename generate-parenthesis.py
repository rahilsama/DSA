#22. Generate Parenthesis
#Given n pairs of parentheses,write a function to generate all combinations of well-formed parentheses


from collections import deque

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        list_balanced = []
        #base case if n is 1
        if n==1:
            list_balanced.append("()")
            return list_balanced
        
        
        
        l = ""
        r = ""
        
        for k in range(n):
            l = l+'('
            r = r+')'
        root = l+r
        list_balanced.append(root)
        
        
        
        
        for i in range(1,(n*2)-1):
            x = root
            # print(list(x))
            char_list = list(x)
            # print("Before:",char_list)
            if char_list[i] == '(':
                char_list[i] = ')'
            else:
                char_list[i] = '('
            
            # print("After: ",char_list)
            if checkBalanced(char_list):
                s = ''.join(char_list)
                print('WORKS')
                if s in list_balanced:
                    continue
                else:
                    list_balanced.append(s)
    
            
            
            for j in range(1,(n*2)-1):
                # print("Before:",char_list)
                char_list2 = char_list.copy()
                if j==i:
                    continue
                else:
                    if char_list2[j] == '(':
                        char_list2[j] = ')'
                    else:
                        char_list2[j] = '('
                    # print(char_list2)
                    if checkBalanced(char_list2):
                        s = ''.join(char_list2)
                        print(s)
                        if s in list_balanced:
                            continue
                        else:
                            list_balanced.append(s)
                # print("After:",char_list2)
                        
        
        
        return list_balanced
    
    

def combinations(list_balanced:list[str], char_list:list[chr], i_start:int, i_end:int ) -> list(str):
    if i_start == i_end:
        
    
    
        
    
def checkBalanced(char_list:list[chr]) -> bool:
    queue = deque()
    s = ''.join(char_list)
    print(s)
    # print("Length of str:",len(s))
    for char in s:
        if char == '(':
            queue.append(char)
        else:
            if queue:
                queue.popleft()
            else:
                return False
    if queue:
        return False
    else:
        return True
    
    
if __name__ == "__main__":
    solution = Solution()
    n = 4
    set = solution.generateParenthesis(n)
    # check = checkBalanced(list("()()()()"))
    print("The possible combinations:", set)