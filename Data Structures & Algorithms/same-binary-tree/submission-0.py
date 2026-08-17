# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def isSameNode(p, q):

            if(not p and not q):
                return True
            if(not p or not q):
                print('here?')
                return False

            right = isSameNode(p.right, q.right)
            left = isSameNode(p.left, q.left)
            
            if(not right or not left ):
                print('or here?')
                return False

            
            if(p.val != q.val):
                print(p.val, q.val)
                print('maybe here?')
                return False

            return True

        return isSameNode(p, q)
