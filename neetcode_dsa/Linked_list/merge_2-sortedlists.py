from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        trial = dummy

        while list1 and list2:
            if list1.val < list2.val:
                trial.next = list1
                list1 = list1.next
            else:
                trial.next = list2
                list2 = list2.next
            trial = trial.next

        if list1:
            trial.next = list1
        elif list2:
            trial.next = list2
            
        return dummy.next

# --- Helper functions for local testing ---
def create_linked_list(arr):
    if not arr: return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def print_linked_list(node):
    vals = []
    while node:
        vals.append(node.val)
        node = node.next
    print(vals)

if __name__=="__main__":
    sol = Solution()
    
    # Create REAL Linked Lists from arrays
    l1 = create_linked_list([1,2,4])
    l2 = create_linked_list([1,3,5])
    
    result = sol.mergeTwoLists(l1, l2)
    print_linked_list(result)

    

        