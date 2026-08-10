# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def bfs(root):
            if not root:
                return 0

            right = bfs(root.right)
            left =  bfs(root.left)

            if root.right:
                right += 1 
            if root.left:
                left += 1 
            
            self.diameter = max(self.diameter, right + left)
            return max(right, left)

        bfs(root)
        return self.diameter