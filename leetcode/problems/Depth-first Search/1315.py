'''
Sum of Nodes with Even-Valued Grandparent
<T> depth-first search  <T> tree



given: binary_tree root
    return: sum of valeus of nodes
        -> only even valued grandparent.
        -> if no nodes are available return 0
        
if x->parent->parent % 2 == 1:
    return val
else: 
    return 0
    
-> If no grandparent exists, just return 0



# We can go with dfs, when traversing we are keeping the status of the grandfather and father
kept values
grand -> grandfather
parent -> father


if grand is none:
    # set current as grand
else:
    if father is None:
        # set current as father
    else:
        left = dfs(curr.left, father, grand)
        right = dfs(curr.right, father, grand)
        
        # set father as grandfather
        # set current as father



return (grand %2 == 1) +  left + right


'''



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        
        def dfs(node, father, grand):
            
            if not node: 
                return 0
            
            if not father:
                father = node.val
                score = 0
            else:
                if grand:
                    score = (grand %2 == 0) * node.val
                else:
                    score = 0
    
                # set father as grandfather
                grand = father
                father = node.val
                
            left = dfs(node.left, father, grand)
            right = dfs(node.right, father, grand)
                
                
            return score + left + right
                
        return dfs(root, None, None)
        