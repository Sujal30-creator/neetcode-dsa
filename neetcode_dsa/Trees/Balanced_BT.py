# Definition for a binary tree node.
from typing import Optional
from BT_Inorder_Traversal import build_tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def height(self,node):
        if not node:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))  
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left_height = self.height(root.left)
        right_height = self.height(root.right)

        balanced_ht = abs(left_height-right_height)

        if balanced_ht <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False

if __name__=="__main__":
    sol = Solution()

    root = build_tree([1,2,2,3,3,None,None,4,4])

    ans = sol.isBalanced(root)
    print(ans)


