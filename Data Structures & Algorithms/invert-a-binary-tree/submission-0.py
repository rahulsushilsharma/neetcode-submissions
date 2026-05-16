# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rev(self , root:Optional[TreeNode]):

        if root == None:
            return
        if root.left == None and root.right == None:
            return 
        
        temp  = root.right
        root.right = root.left
        root.left = temp

        self.rev(root.right)
        self.rev(root.left)
        return 
            
        
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        head = root
        self.rev( root)
        return head