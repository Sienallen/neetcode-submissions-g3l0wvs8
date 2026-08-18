# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root:
            return False
        
        def isIdentical(root, subRoot):

            if not subRoot and not root:
                return True
            if not subRoot or not root:
                return False
            
            if(subRoot.val == root.val):

                left = isIdentical(root.left, subRoot.left)
                right = isIdentical(root.right, subRoot.right)

                return left and right

            return False


        if(root.val == subRoot.val ):
            if(isIdentical(root, subRoot)):
                return True

        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        if left or right:
            return True
        
        return False

        
