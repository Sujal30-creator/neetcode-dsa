from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        tail = dummy
        hashmap = {}

        # Store nodes grouped by their values
        for head in lists:
            curr = head
            while curr:
                nxt = curr.next          # Save next before disconnecting
                curr.next = None         # Break old link
                hashmap.setdefault(curr.val, []).append(curr)
                curr = nxt

        # Reconnect nodes in sorted order
        for key in sorted(hashmap.keys()):
            for node in hashmap[key]:
                tail.next = node
                tail = node

        tail.next = None
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

if __name__ == "__main__":
    sol = Solution()
    lists = [
        # build_linked_list([1, 4, 5]),
        # build_linked_list([1, 3, 4]),
        # build_linked_list([2, 6])
        build_linked_list([])
    ]

    sol = Solution()
    ans = sol.mergeKLists(lists)

    print_linked_list(ans)
