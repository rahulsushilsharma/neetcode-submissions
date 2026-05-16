# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def check(self, node, min_val, max_val):
        if not node:
            return True

        if not (min_val < node.val < max_val):
            return False

        left = self.check(node.left, min_val, node.val)
        right = self.check(node.right, node.val, max_val)
        return left and right

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.check(root, float('-inf'), float('inf'))