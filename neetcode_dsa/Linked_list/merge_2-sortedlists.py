from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 ,curr2 = list1, list2

        while curr1:
            if curr1.val >= curr2.val:
                nxt = curr2.next
                prev.next = curr2
                curr2.next = curr1
                curr2 = nxt
            else:
                prev = curr1
                curr1 = curr1.next

if __name__=="__main__":
    sol = Solution()
    print(sol.mergeTwoLists(list1=[1,2,4],list2=[1,3,5]))

    

        