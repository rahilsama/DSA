#3. Longest substring without repeating characters

# would like to try using hash maps cause it is all about efficiently INSERT and SEARCH chars
# Update: Scratch that idea. i will try with QUEUES

from collections import deque


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        queue = deque()
        highest = 0
        count = 0 
        
        for char in s:      
            if char in queue:
                #if character is being repeated
                while queue:
                    if queue[0] == char:
                        queue.popleft()
                        break
                    queue.popleft()
            queue.append(char) 
                    
            count = len(queue)
            highest = max(highest, count)
            # print("Longest:",queue)  
        return highest      
                    



def main():
    solution = Solution()
    user_input = input("Enter a string: ")
    result = solution.lengthOfLongestSubstring(user_input)
    print(f"Length of longest substring without repeating characters: {result}")


if __name__ == "__main__":
    main()