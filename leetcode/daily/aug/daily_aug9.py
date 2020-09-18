'''

We can iterate the grid directly


# If all rotten
    return 0

Recursive
# If you find a rotten one, mark other directions as rotten. 
# Increase time


def algorithm(grid):   
    time = 0
    marked = True
    while marked:
        marked = False
        # 1 single iteration
        for row in range(len(grid)):
            for col in range(len(grid[row])):

                item = grid[row][column]
                if item == 2:
                    marked += markRotten(grid, row, col -1 )
                    marked += markRotten(grid, row -1, col)
                    marked += markRotten(grid, row +1, col)
                    marked += markRotten(grid, row, col +1 )

            if marked == False:
                return time
            else:
                time += 1
    return time

# Mark rotten if it is a normal apple
def markRotten(grid, row, col):
    if grid[row][col] == 1:
        grid[row][col] = 2
        return 1
    return 0

'''

import copy

class Solution:
    
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        
        def dumpGrid(grid):
            for row in grid:
                print(row)
        
        def markRotten(grid, row, col, max_row, max_col):
            if row > max_row:
                return 0
            if col > max_col:
                return 0
            if row < 0 or col <0:
                return 0

            
            if grid[row][col] == 1:      
                grid[row][col] = 2
                         
                print(row, col,"->done")
                dumpGrid(grid)
                return 1
            return 0
        
        dumpGrid(grid)
        
        grid_mark = copy.deepcopy(grid)
        
        time = 0
        marked = 1
        while marked:
            fresh_exists = False
            marked = 0
            # 1 single iteration
            for row in range(len(grid)):
                max_row = len(grid)-1
                
                
                for col in range(len(grid[row])):
                    max_col = len(grid[row])-1
                    item = grid[row][col]
                    
                    if item == 1:
                        fresh_exists = True
                    
                    if item == 2:
                        marked += markRotten(grid_mark, row, col-1, max_row, max_col)
                        marked += markRotten(grid_mark, row-1, col, max_row, max_col)
                        marked += markRotten(grid_mark, row+1, col, max_row, max_col)
                        marked += markRotten(grid_mark, row, col+1, max_row, max_col)
                        
                        
            if marked == 0:
                #time += 1

                # If there exists a not rotten apple, then not possible at this point
                # return -1
                if fresh_exists:
                    return -1
                else: 
                    return time
            else:
                time += 1
                
            print("Iteration finished", time)
            grid = copy.deepcopy(grid_mark)
                    

'''
[[2,1,1],[0,1,1],[1,0,1]]
Output:
4
Expected:
-1


Input:
[[2,1,1],[1,1,0],[0,1,1]]
Output:
5
Expected:
4
'''

