from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bfsTraversal(self, root: Optional[TreeNode]) -> list[int]:
        sol = list()

        if not root:
            return sol
        
        queue = deque([root])

        while queue:
            node = queue.popleft()
            sol.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return sol