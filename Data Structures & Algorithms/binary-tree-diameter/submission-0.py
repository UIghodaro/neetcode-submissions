# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    maxDiam = 0

    def findDepth(self, root: Optional[TreeNode]) -> int:
        left, right = 0, 0
        if root is not None:
            left = self.findDepth(root.left)
            right = self.findDepth(root.right)
            print(left, right)

            if left + right > self.maxDiam:
                self.maxDiam = left + right
        
        else:
            return 0
        
        return 1 + max(left, right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.findDepth(root)

        return self.maxDiam
    

        

