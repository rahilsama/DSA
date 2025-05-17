#22. Generate Parenthesis
#Given n pairs of parentheses,write a function to generate all combinations of well-formed parentheses


from collections import deque

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def backtrack(current, open_count, close_count):
            print(current)
            # Base case: when the string is complete
            if len(current) == 2 * n:
                result.append(current)
                return
            
            # Add '(' if we still have some left
            if open_count < n:
                backtrack(current + '(', open_count + 1, close_count)
            
            # Add ')' if it won't exceed the number of '('
            if close_count < open_count:
                backtrack(current + ')', open_count, close_count + 1)
        
        backtrack('', 0, 0)
        return result
    
    
def generate_parentheses(n):
    result = []

    def backtrack(current, open_count, close_count):
        print(current)
        # Base case: when the string is complete
        if len(current) == 2 * n:
            result.append(current)
            return
        
        # Add '(' if we still have some left
        if open_count < n:
            backtrack(current + '(', open_count + 1, close_count)
        
        # Add ')' if it won't exceed the number of '('
        if close_count < open_count:
            backtrack(current + ')', open_count, close_count + 1)
    
    backtrack('', 0, 0)
    return result

# Example usage
n = 3
combinations = generate_parentheses(n)
print(combinations)


# def combinations(list_balanced:list[str], char_list:list[chr], i_start:int, i_end:int ) -> list(str):
#     if i_start == i_end:
        
    
    
        
    
# def checkBalanced(char_list:list[chr]) -> bool:
#     queue = deque()
#     s = ''.join(char_list)
#     print(s)
#     # print("Length of str:",len(s))
#     for char in s:
#         if char == '(':
#             queue.append(char)
#         else:
#             if queue:
#                 queue.popleft()
#             else:
#                 return False
#     if queue:
#         return False
#     else:
#         return True
    
    
# if __name__ == "__main__":
#     solution = Solution()
#     n = 4
#     set = solution.generateParenthesis(n)
#     # check = checkBalanced(list("()()()()"))
#     print("The possible combinations:", set)