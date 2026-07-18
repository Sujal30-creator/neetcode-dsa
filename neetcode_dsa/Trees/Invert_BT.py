from typing import Optional
from BT_Inorder_Traversal import build_tree

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
    
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def invert(node):
            if not node:
                return
            node.left, node.right = node.right, node.left
            invert(node.left)
            invert(node.right)

        invert(root)
        return root



if __name__=="__main__":
    root = build_tree([])

    sol = Solution()
    ans = sol.invertTree(root)

    vans = sol.inorderTraversal(ans)

    print(vans)
