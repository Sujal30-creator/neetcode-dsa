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
    def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        res = list()

        def postorder(root):
            if not root:
                return
            postorder(root.left)
            postorder(root.right)
            res.append(root.val)

        postorder(root)
        return res

if __name__ == "__main__":
    root = build_tree([1, 2, 3, None, 4, 5, None])

    sol = Solution()
    ans = sol.postorderTraversal(root)

    print(ans)