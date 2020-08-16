'''
Deepest Leaves Sum
<T> Depth-First-Search <T> Tree


Return the sum of the deepest leaves.
firstly: We will run dfs to determine max depth O(n)
secondly: We will run another dfs to get the sum of elems in that depth O(n)


# It would be better to keep a hashmap when traversing such as 
depth->arr<vals> then sum it


'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None or root == []:
            return 0
        
        def search_dfs(node, depth):
            
            
            depth = depth +1
            
            # Base Case
            if node.left is None and node.right is None:
                return depth
            
            
            left = 0
            right = 0
            if node.left:
                left = search_dfs(node.left, depth)
            
            if node.right:
                right = search_dfs(node.right, depth)
            
            return max(left,right)
            
                
        max_found = search_dfs(root, 0)
        #print("max depth: ", max_found)
        
        def sum_dfs(node, depth, max_depth):
            
            end_val = 0
            
            depth = depth +1
            
            if depth == max_depth:
                return node.val
            
            # Base Case
            if node.left is None and node.right is None:
                return 0
            
            if node.left:
                end_val += sum_dfs(node.left, depth, max_depth)
            
            if node.right:
                end_val +=  sum_dfs(node.right, depth, max_depth)
            
            return end_val
        
        return sum_dfs(root, 0, max_found)
        