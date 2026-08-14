from typing import Optional
from BT_Inorder_Traversal import build_tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def traverse(self,node, sol: list):
    #     if not node:
    #         sol.append(None)
    #         return
    #     sol.append(node.val)
    #     self.traverse(node.left, sol)
    #     self.traverse(node.right, sol)

    # def isSameTree(self, p: Optional[TreeNode], sol2: list) -> bool:
    #     sol1 = list()

    #     self.traverse(p,sol1)
        
    #     if sol1 == sol2:
    #         return True
    #     return False
    
    # def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]):
        
    #     if not root:
    #         return False
        
    #     if not subRoot:
    #         return True
        
        
    #     sol = list()
    #     self.traverse(subRoot, sol)

    #     return (
    #         self.isSameTree(root, sol)
    #         or self.isSameTree(root.left, sol)
    #         or self.isSameTree(root.right, sol)
    #     )
    def isSameTree(self, p, q):
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return (
            self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )


    def isSubtree(self, root, subRoot):
        if not subRoot:
            return True

        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True

        return (
            self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )

        

if __name__=="__main__":
    root = build_tree([1,2,3,4,5])
    sub_root = build_tree([2,4,5])

    sol = Solution()
    ans = sol.isSubtree(root, sub_root)
    print(ans)
