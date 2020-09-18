'''

inorder = l, c, r
postorder = l, r, c

Analysis
inorder -> take l, take c stack[r1] ll stack[r2] .... return r2.r1

postorder -> take l, take ll, take lll, backtrack, take llr, take ll


Algorithm
def algorithm():
    root = inorder[0]
    #if root have left node?
    # then inorder[1] == postorder[0]
    
    if inorder[1] == postorder[0]:
        left_child = inorder[1]
        
    else:
        right_child = inorder[1]



two children
  a
 !  !
 b  c
 

only left child
  a
 !   
 b



only right child
    a
      !
      c




no childs
    a

'''

'''
Above is not working, another analysis

inorder
# l, center, r  bottom to top

if we reverse the postorder
# center, r, l top to bottom


we can compare those to build a tree
lets assume there is a level delimiter between l and r


    3
   / \
  9  20

in       3 9 20
rev-post 3 9 20

   3
   / \
  9  20
    /  \
   15   7

ino =        9   3   15  20  7
post =       9   15  7   20  3
rev-post =   3   20  7   15  9


levels, a, b, c
try to place limiters
ino =        9b   3a   15c  20b   7c
rev-post =   3a   20b  7c   15c   9b


We need to estimate, a , b and c levels from above
to get a definitive estimate

- l, c, r   
- c, r, l

 
- rev_post[0] --> root node

Then we search until the in[k] = root
Then in[1:k] is the left side.

Let's try it
rev_post[0] = 3a
in[1] = 3a
in[0:] = 9b --> left part

Lets remove processed center and left to go right
ino         = 15c 20b 7c
rev-post    = 20b 7c 15c

20b is the new root.
left_side is the until 20b in ino
root -> 20b
left -> ..15c
right -> 7c

'''
'''
This is working and possible to recurse,
but we need a decent example on the left part to determine recursion, 
I'll extend left side

        3
      /    \
     9      20
    / \     / \
   26  2   15  7

ino     l, c, r
post    l, r, c

ino      26c, 9b, 2c, 3a, 15c, 20b, 7c
post     26c, 2c, 9b, 15c, 7c, 20b, 3a
rev-post 3a, 20b, 7c, 15c, 9b, 2c, 26c

ino      26c, 9b, 2c, 3a, 15c, 20b, 7c
rev-post 3a, 20b, 7c, 15c, 9b, 2c, 26c

First round
center -> revpost[0] = 3a
        search ino[pos] = 3a, get pos
left -> ino[:pos] = 26c, 9b, 2c
        rev-post[size-pos:]
right -> ino[pos:] = 15c, 20b, 7c
        revpost[1:size-pos]
recursively add nodes

do with pos, no need to reverse it
ino      26c, 9b, 2c, 3a, 15c, 20b, 7c
post     26c, 2c, 9b, 15c, 7c, 20b, 3a

center -> post[-1] = 3a
        search ino[k] = 3a, get k
        
left -> ino[:k] = 26c, 9b, 2c
        post[:k]
right -> ino[k:] = 15c, 20b, 7c
        post[k:-1]
'''




# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        
        #inorder = [26, 9, 2, 3, 15, 20, 7]
        #postorder = [26, 2, 9, 15, 7, 20, 3]
        
        #print(inorder)
        #print(postorder)
        
        root = TreeNode()
        return self.dfs(root, inorder, postorder)
        
    def dfs(self, root, ino, post):
        
        # base case
        if len(post) == 0 or len(ino) == 0:
            return None
        
        root.val = post[-1]
        
        #print(root.val)
        #print(ino)
        #print(post)
        
        # Find k
        for i in range(len(post)):
            if (ino[i] == root.val):
                k = i
                break
                
        
        
        # Left recursion, if exists
        left_ino = ino[:k]
        left_post = post[:k]
        left = TreeNode()
        root.left = self.dfs(left, left_ino, left_post)
        
        # Right recursion, if exists
        right_ino = ino[k+1:]
        right_post = post[k:-1]
        right = TreeNode()
        root.right = self.dfs(right, right_ino, right_post)
        
        return root
        
        