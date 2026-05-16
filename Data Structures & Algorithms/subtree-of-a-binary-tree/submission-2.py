# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def comp(self, tree1, tree2):
        if tree1 == None and tree2 == None:
            return True
        
        if tree1 == None or tree2 == None:
            return False
        
        if tree1.val != tree2.val:
            return False
        
        left  = self.comp(tree1.left, tree2.left)
        right = self.comp(tree1.right , tree2.right)

        return left and right
    
    def ittr(self, tree1, tree2):
        if tree1 == None :
            return False
        if tree1.val == tree2.val  and self.comp(tree1, tree2):
            return True
        left = self.ittr(tree1.left, tree2)
        right= self.ittr(tree1.right, tree2)

        return left or right
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.ittr(root, subRoot)