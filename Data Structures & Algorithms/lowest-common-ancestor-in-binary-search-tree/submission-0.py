# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def tra(self, root, node1, node2):
        if root == None or not node1 or not node2:
            return None
        if (max(node1.val, node2.val)<root.val):
            return self.tra(root.left, node1, node2)
        elif (min(node1.val, node2.val) > root.val):
            return self.tra(root.right , node1, node2)
        else:
            return root
        

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        return self.tra(root,p,q)