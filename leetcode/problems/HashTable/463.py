'''
Island Perimeter
<T> HashTable


Map in form a two-dimensional grid
1 -> land
0 -> water

# Grid cells are connected horizontally/vertically 
# Grid is completely surrounded by water, and there is exactly one island
--> Does not include lakes


# Traverse the grid
# Add 4 for each land default
# If there is a neighbor above or left, subtract 2

'''



class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        score = 0
        
        for h in range(len(grid)):
            for v in range(len(grid[h])):
                if grid[h][v] == 1:
                    score += 4
                    
                    if h>0 and grid[h-1][v] == 1:
                        score -= 2

                    if v>0 and grid[h][v-1] == 1:
                        score -= 2 
                                    
        return score