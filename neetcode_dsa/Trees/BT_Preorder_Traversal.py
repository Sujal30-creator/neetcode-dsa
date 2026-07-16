from typing import Optional
from collections import deque
from BT_Inorder_Traversal import build_tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        res = list()

        def preorder(root):
            if not root:
                return
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)
        
        preorder(root)
        return res

if __name__ == "__main__":
    root = build_tree([1, 2, 3, None, 4, 5, None])

    sol = Solution()
    ans = sol.preorderTraversal(root)

    print(ans)