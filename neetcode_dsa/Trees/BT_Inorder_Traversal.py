from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        sol = list()

        def inorder(root):
            if not root:
                return []
            inorder(root.left)
            sol.append(root.val)
            inorder(root.right)
            
            return sol
        
        inorder(root)
        return sol

def build_tree(arr):
    """
    Builds a binary tree from a level-order list.
    Example:
    [1, None, 2, 3]

        1
         \
          2
         /
        3
    """
    if not arr:
        return None

    root = TreeNode(arr[0])
    q = deque([root])
    i = 1

    while q and i < len(arr):
        node = q.popleft()

        # Left child
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            q.append(node.left)
        i += 1

        # Right child
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            q.append(node.right)
        i += 1

    return root

if __name__ == "__main__":
    
    root = build_tree([1, 2, 3, None, 4, 5, None])

    sol = Solution()
    ans = sol.inorderTraversal(root)

    print(ans)