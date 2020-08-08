'''
Vertical Order Traversal

inp| root:Node --> given root of binary tree
out| int[int[]] --> Traversal results

Constraints:
-> Each node has (x,y) coordinate
-> Root has (x,y) left node (x-1,y-1), right node(x+1,y+1)
-> Traversal results left to right x-m,....,x,.....x+l
-> Results have an order of decreasing y values

-> Tree has n = 1-1000 nodes
-> Each node val in (0,1000)

-> If two nodes have same x and same y, the one with smaller val comes first

# Naive solution, Traverse with a bfs
# Bfs handles the decreasing y values
# Keep and n=1000 array or x coordinates.
# Root starts at 500



# Rough BFS solution, doesn't evaluate when same x=y occurance
# We still need to keep the y's in mind
from collections import deque

self.x_arr = []

def bfs(self, root):
    
    queue = deque()
    queue.append(root,0)
    processed = [[] for i in range(1000)]
    
    while queue != []:
        current,x = queue.popleft()
        if current->left is not None:
            if not current->left in processed:
                x = x-1
                queue.append(current->left)
        if current->right is not None:
            if not current->right in processed:
                x = x+1
                queue.append(current->right)
        
        processed[x].append(current)
        
    
# DFS solution, hold x and y values
# Includes sorting to x first, y second, then node value. 
    
# each node has (x,y,val)
# groupby(x) --> sort y --> sort val
# renzhang's description is used https://www.youtube.com/watch?v=N-eSD_NZWXA

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        # x-> (y,val) tuple
        hmap = collections.defaultdict(list)
    
        def dfs(node,x,y):
            hmap[x].append((y,node.val))
            if node.left: dfs(node.left, x-1, y+1)
            if node.right: dfs(node.right, x+1, y+1)
        
        dfs(root,0,0)
        return [[x[1] for x in sorted(hmap[i])] for i in sorted(hmap)] 
        