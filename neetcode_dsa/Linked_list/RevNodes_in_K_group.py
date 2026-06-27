from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def revList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        counter = 0
        dummy = ListNode(val=-1,next = head)
        curr = dummy

        while curr:
            if counter == 0:
                prev, start = curr, curr.next

            elif counter == k:
                end, after = curr, curr.next
                end.next = None
                new_head = self.revList(start)
                prev.next, start.next = new_head, after
                counter = 0
                curr = start
                continue

            curr = curr.next
            counter+=1
        return dummy.next


def build_linked_list(arr):
    dummy = ListNode()
    curr = dummy
    for num in arr:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next


def print_linked_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")

if __name__=="__main__":
    sol = Solution()
    arr = [1,2,3,4]
    ans = sol.reverseKGroup(build_linked_list(arr), k=3)
    print_linked_list(ans)


