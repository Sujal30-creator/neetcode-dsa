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
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

if __name__=="__main__":
    root = build_tree([1,2,3,None,None,4])

    sol = Solution()
    ans = sol.maxDepth(root)

    print(ans)
