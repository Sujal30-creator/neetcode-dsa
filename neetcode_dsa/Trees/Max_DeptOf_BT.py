from typing import Optional
from BT_Inorder_Traversal import build_tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        pass

if __name__=="__main__":
    root = build_tree([])

    sol = Solution()
    ans = sol.maxDepth(root)

    vans = sol.inorderTraversal(ans)

    print(vans)
