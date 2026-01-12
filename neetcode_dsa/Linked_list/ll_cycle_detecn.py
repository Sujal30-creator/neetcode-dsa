# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #O(N) --> Time & Space Complexity
        # ptr = head
        # hashmap = set()

        # while ptr:
        #     if ptr in hashmap:
        #         return True
        #     else:
        #         hashmap.add(ptr)
        #         ptr = ptr.next
        # return False


        #O(N), O(1) --> Time, Space Complexity

        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next

            fast = fast.next.next

            if slow == fast:
                return True
            
        return False

# --- Helper to create a list with a cycle ---
def create_cycled_list(arr, pos):
    if not arr: return None
    
    head = ListNode(arr[0])
    curr = head
    cycle_entry_node = None
    
    # Save reference to the node at index 'pos' if pos is 0
    if pos == 0:
        cycle_entry_node = head

    # Build the list
    for i in range(1, len(arr)):
        curr.next = ListNode(arr[i])
        curr = curr.next
        
        # Save reference to the cycle entry node
        if i == pos:
            cycle_entry_node = curr
    
    # Create the cycle: Point the last node back to the saved node
    if pos != -1 and cycle_entry_node:
        curr.next = cycle_entry_node
        
    return head

if __name__=="__main__":
    sol = Solution()
    
    # Example 1: Head = [3,2,0,-4], pos = 1 (Tail connects to index 1)
    # The list looks like: 3 -> 2 -> 0 -> -4
    #                           ^_________|
    
    list_with_cycle = create_cycled_list([3, 2, 0, -4], 1)
    print(f"Has Cycle: {sol.hasCycle(list_with_cycle)}") # Should be True
    
    # Example 2: No Cycle
    list_no_cycle = create_cycled_list([1, 2, 3], -1)
    print(f"Has Cycle: {sol.hasCycle(list_no_cycle)}") # Should be False
        