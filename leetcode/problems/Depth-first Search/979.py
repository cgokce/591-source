'''
Distribute Coins in Binary Tree
<T> Depth-first Search

N node binary tree
    each node has node.val coins
    Total N coins
    node can be 0
    
In a move
    May choose two adjacent nodes and move one coin to other
    return number of moves required to make every node have exactly one coin


Solution:
- If a node have coin>0 we can distribute it until no coin left 
If we do a dfs, when we encounter node>0
    - we can firstly check and distribute coins to the left and right nodes
    - then we can distribute coins to the upwards
but this does not guarantee equal dist


# better solution
- there is a guarantee, a node needs total coin count of chilren + 1(self)
- easiest movement is moving coins to the root then distribute to children
    - unless chilren itself has the coin
    


so for the dfs
    if node == leaf: return 1
    coin_requirement = 1 + dfs(left->child) + dfs(right->child)
    
if node has more than one coin
    it needs to be distributed to children
    then needs to be distributed above
    
We need a bottom to top kind of traversing



so in the dfs

    # This is upward prop
    if coin_req < coin_already_have
        push coin_have - coin_req to the root
        turns += coin_have - coin_req

    # This is downward prop
    # now we have coin_req = coin_have
    if coin > 1:
    
        send_left(coin_left_req)
        send_right(coin_right_req)
        
        
# This can not be done in one traverse
# Needs two traversal


# Using the hints from the solution

# At leaf -> Push coin higher if >1
          -> Take one from root if <1

    excess = Math.abs(num_coins -1)
    
    Afterwards do not consider the leaf again.
    
# Algorithm

# Trick is allowing minus one in the leaf node
excess = Math.abs(num_coins -1)

https://leetcode.com/problems/distribute-coins-in-binary-tree/discuss/221930/JavaC%2B%2BPython-Recursive-Solution
Following Lee's method:
Since node_count = coin count:
For each node its total movement equal to
    we'll return that during the dfs
    x = node.val + -1  + node.left + node.right
    
We are done with the leaf after processed
Bottom up process
So we will hold a global variable that sums every backtrack from left and right
   



'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    score = 0
    
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def dfs(node):
            # base case if node is null
            if not node: return 0
        
            left = dfs(node.left)
            right = dfs(node.right)
            
            # Trick is nodes are allowed to have negative sums, so we'll just abs it out
            self.score += abs(left) + abs(right)
            
            # Return the current node's vals
            return node.val - 1 + left + right
            
            
        _ = dfs(root)
        return self.score
        
        
                