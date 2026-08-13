# Definition for a binary tree node.
from typing import Optional
from BT_Inorder_Traversal import build_tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        sol1 = list()
        sol2 = list()
        
        def traverse(node, sol: list):
            if not node:
                sol.append(None)
                return
            sol.append(node.val)
            traverse(node.left, sol)
            traverse(node.right, sol)

        traverse(p,sol1)
        traverse(q,sol2)
        
        if sol1 == sol2:
            return True
        return False
            
if __name__=="__main__":
    sol = Solution()

    p = build_tree([1,2,1])
    q = build_tree([1,1,2])

    ans = sol.isSameTree(p,q)
    print(ans)


