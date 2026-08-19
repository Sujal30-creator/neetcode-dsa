# Definition for a binary tree node.
from typing import Optional
from collections import deque
from BT_Inorder_Traversal import build_tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bfsTraversal(self, root: Optional[TreeNode]) -> list[int]:
        sol = list()

        if not root:
            return sol
        
        queue = deque([root])

        while queue:
            node = queue.popleft()
            sol.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return sol
    
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            root = TreeNode(val=val, left=None, right=None)
            return root
        
        def findPrev(node, val):
            if node.val > val:
                if node.left:
                    findPrev(node.left, val)
                else:
                    node.left = TreeNode(val = val, left=None, right=None)
            elif node.val <= val:
                if node.right:
                    findPrev(node.right, val)
                else:
                    node.right = TreeNode( val = val, left = None, right=None)

        findPrev(root, val)
                
        return root


            
if __name__=="__main__":
    sol = Solution()

    root = build_tree([5,3,6,None,4,None,10,None,None,7])

    ans = sol.insertIntoBST(root, val=9)

    print(sol.bfsTraversal(ans))


