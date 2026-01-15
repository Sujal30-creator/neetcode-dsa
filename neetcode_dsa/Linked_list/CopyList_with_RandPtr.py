from typing import Optional

# Definition for a Node.

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = dict()

        curr = head

        while curr:
            copy = Node(curr.val)
            hashmap[curr] = copy
            curr = curr.next

        for key,value in hashmap.items():
            if key.next in hashmap:
                value.next = hashmap[key.next]
            if key.random in hashmap:
                value.random = hashmap[key.random]
        
        return hashmap[head]


# --- COMPLEX HELPER TO BUILD LIST WITH RANDOM POINTERS ---
def build_random_list(arr):
    if not arr: return None
    
    # Step 1: Create all nodes and store in a list for index access
    nodes = []
    for item in arr:
        nodes.append(Node(item[0]))
        
    # Step 2: Connect 'next' and 'random' pointers
    for i in range(len(nodes)):
        # Connect Next (if not last node)
        if i < len(nodes) - 1:
            nodes[i].next = nodes[i + 1]
            
        # Connect Random (if index is not None)
        random_index = arr[i][1]
        if random_index is not None:
            nodes[i].random = nodes[random_index]
            
    return nodes[0] # Return the head

if __name__=="__main__":
    sol = Solution()
    
    # 1. Build the complex graph structure
    raw_input = [[3,None],[7,3],[4,0],[5,1]]
    head_node = build_random_list(raw_input)
    
    # 2. Run your solution
    sol.copyRandomList(head_node)