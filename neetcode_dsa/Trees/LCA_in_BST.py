# Definition for a binary tree node.
from typing import Optional
from BT_Inorder_Traversal import build_tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pass
            
if __name__=="__main__":
    sol = Solution()

    root = build_tree([5,3,8,1,4,7,9,None,2])

    ans = sol.lowestCommonAncestor(root,p=3,q=8)
    print(ans)


