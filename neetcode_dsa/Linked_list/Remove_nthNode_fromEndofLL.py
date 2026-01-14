from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummynode = ListNode(val=0, next=head)

        slow = dummynode
        fast = head

        while n>0 and fast:
            fast = fast.next
            n -= 1

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummynode.next #what if head is deleted if the the list has only 1 element and n=1
        


if __name__=="__main__":
    # 1. Add this helper function to convert [1,2,3] -> ListNode
    def build_linked_list(arr):
        dummy = ListNode(0)
        curr = dummy
        for x in arr:
            curr.next = ListNode(x)
            curr = curr.next
        return dummy.next

    sol = Solution()
    
    # 2. Convert the input BEFORE passing it to the function
    raw_list = [1,2,3,4,5,6]
    head_node = build_linked_list(raw_list)
    
    # 3. Now pass the ListNode object
    print(sol.removeNthFromEnd(head=head_node, n=1))