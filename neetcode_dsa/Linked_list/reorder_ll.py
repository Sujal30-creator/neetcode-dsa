from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # Catching Middle
        slow = head
        fast = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        if fast:
            temp = slow.next
            slow.next = None
            slow = temp
        else:
            prev.next = None

        #Reversing the sub-array
        print('Before reversing:' + str(slow.val))

        prev = None

        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        print('After reversing:' + str(prev.val))

        #Merging into the final arr
        
        while head and prev:
            dummy1 = head.next
            dummy2 = prev.next
            head.next = prev
            prev.next = dummy1
            head = dummy1
            prev = dummy2

        print('Last node:' + str(head.val))




def build_linked_list(arr):
    dummy = ListNode()
    curr = dummy
    for x in arr:
        curr.next = ListNode(x)
        curr = curr.next
    return dummy.next

if __name__ == "__main__":
    sol = Solution()
    head = build_linked_list([0,1,2,3,4,5,6])
    sol.reorderList(head)
    
        
