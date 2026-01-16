from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1, ptr2 = l1, l2

        num1 = ''
        num2 = ''

        while ptr1 :
            num1 = str(ptr1.val) + num1
            ptr1 = ptr1.next

        while ptr2:
            num2 = str(ptr2.val) + num2
            ptr2 = ptr2.next

        ans = int(num1) + int(num2)
        ans = str(ans)

        head = None

        for i in range(len(ans)):
            newNode = ListNode(int(ans[i]))
            newNode.next = head
            head = newNode

        return head


# Helper function to convert a list to a ListNode (singly-linked list)
def list_to_linkedlist(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert a ListNode to a list
def linkedlist_to_list(node):
    arr = []
    while node:
        arr.append(node.val)
        node = node.next
    return arr

if __name__=="__main__":
    sol = Solution()

    # Convert lists to ListNode objects
    l1_linked = list_to_linkedlist([1,2,3])
    l2_linked = list_to_linkedlist([4,5,6])
    print(sol.addTwoNumbers(l1 = l1_linked, l2 = l2_linked))
