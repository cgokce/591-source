'''

Path Sum III

Naive approach
- doing dfs, there will be sum at each node, that returns 1
- if sum>n return 0

# 10,
# 10, 5 --> 15, 5
    # 3 --> 18, 8, 3
    # 2 --> 7, 2

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        
        def dfs(node, totals, n):
            
            final_sum = 0
            
            #print(node, total, n)
            if node is None:
                #print("return empty")
                return final_sum
            
            totals.append(0)
            totals = [i+node.val for i in totals]
            
            #totals_path = [totals[i] - totals[i+1] for i in range(len(totals)-1)]
            #print(totals_path, node.val)
            
            for a in totals:
                if a == n:
                    #print("found 1")
                    final_sum += 1
                    
            final_sum += dfs(node.left, totals.copy(), n) + dfs(node.right, totals.copy(), n)
            
            return final_sum
            
        return dfs(root, [], sum)
            