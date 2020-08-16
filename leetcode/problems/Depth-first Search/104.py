'''
Maximum Depth of Binary Tree
<T> Depth-First Search <T> Tree

Given a binary tree, find it's maximum length

# We will do a dfs
# Branches left and right
# Base case: And return the depth when leaf is accessed

'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if root is None or root == []:
            return 0
        
        def dfs(node, depth):
            # Base
            if node.left == None and node.right == None:
                return depth
            
            left = 0
            right = 0
            if node.left:
                left = dfs(node.left, depth+1)
            if node.right:
                right = dfs(node.right, depth+1)
            
            return max(left, right)
        
        return dfs(root, 1)
            
            
            
        