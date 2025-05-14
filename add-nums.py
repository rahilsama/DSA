from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        flag = False
        l3 = None
        
        #i wanna check which one of the list is bigger and which is smaller
        while l1 and l2:
            # print("TEST")
            num1 = l1.val
            num2 = l2.val
            total = 0
            total = num1+num2
            # print("Pre loop total:",total)
            
            
            if flag:
                total+=1
                flag = False
                # print(total)
                
            # print("After flag check: ",total)
                
            if total > 9:
                flag = True
                total = total-10
                # print("TEST")
                if l3:
                    # print("if loop: ",total)
                    end_of_list(l3).next = ListNode(total)
                else:
                    l3 = ListNode(total)
            else:
                if l3:
                    # print("else loop: ",total)
                    end_of_list(l3).next = ListNode(total)
                else:
                    l3 = ListNode(total)
                
            l1 = l1.next
            l2 = l2.next
            if not l1 and not l2 and flag:
                end_of_list(l3).next = ListNode(1)
                break
        
        if l1 or l2:
            if l1:
                while l1:
                    num = l1.val
                    if flag:
                        num+=1
                        flag = False
                        # print(total)
                    if num > 9:
                        flag = True
                        num = num-10
                        # print("TEST")
                        if l3:
                            print("if loop: ",num)
                            end_of_list(l3).next = ListNode(num)
                        else:
                            l3 = ListNode(num)
                    else:
                        if l3:
                            print("else loop: ",num)
                            end_of_list(l3).next = ListNode(num)
                        else:
                            l3 = ListNode(num)
                        
                    l1 = l1.next
                    if not l1 and flag:
                        end_of_list(l3).next = ListNode(1)
                        break
            else:
                while l2:
                    num = l2.val
                    if flag:
                        num+=1
                        flag = False
                        # print(total)
                    if num > 9:
                        flag = True
                        num = num-10
                        # print("TEST")
                        if l3:
                            print("if loop: ",num)
                            end_of_list(l3).next = ListNode(num)
                        else:
                            l3 = ListNode(num)
                    else:
                        if l3:
                            print("else loop: ",num)
                            end_of_list(l3).next = ListNode(num)
                        else:
                            l3 = ListNode(num)
                        
                    l2 = l2.next
                    if not l2 and flag:
                        end_of_list(l3).next = ListNode(1)
                        break

                
        print_linked_list(l3)
        return l3
            
            
                
                
def main():
    solution = Solution()
    
    l1 = Optional[ListNode]
    l2 = Optional[ListNode]
    
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    
    
    print_linked_list(l1)
    x = end_of_list(l2)
    # print(x.val)
    print_linked_list(l2)
    
    
    result = solution.addTwoNumbers(l1, l2)
    # print_linked_list(result)


def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    print()
    
# write a func that returns the end of the list
def end_of_list(head: Optional[ListNode]) -> ListNode: 
    current = head
    while current:
        if current.next == None:
            break
        else:
            current = current.next
    return current

if __name__ == "__main__":
    main()
        