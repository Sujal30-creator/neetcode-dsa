# Definition for a binary tree node.
from typing import Optional
from BT_Inorder_Traversal import build_tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # O(n^2)
    # def height(self,node):
    #     if not node:
    #         return 0
    #     return 1 + max(self.height(node.left), self.height(node.right))
        
    # def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0
        
    #     left_height = self.height(root.left)
    #     right_height = self.height(root.right)

    #     curr_diam = left_height + right_height

    #     left_diameter = self.diameterOfBinaryTree(root.left)
    #     right_diameter = self.diameterOfBinaryTree(root.right)

    #     return max(curr_diam, left_diameter, right_diameter)

    # O(n)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res

            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left+right)

            return 1 + max(left,right)
        
        dfs(root)
        return res

        

if __name__=="__main__":
    sol = Solution()

    root = build_tree([1,None,2,3,4,5])

    ans = sol.diameterOfBinaryTree(root)
    print(ans)


