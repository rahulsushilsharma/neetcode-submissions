# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def tra(self, cur, root):
        if root == None:
            return cur
       
        left = self.tra(cur,root.left)
        right = self.tra(cur,root.right)
        
        return 1 + max(left, right) 
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        cur = 0
        cur = self.tra(cur, root)
        return cur