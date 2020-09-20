'''
Grid traversal 
-> dfs
-> backtracking


Backtracking
-> State machine
-> Where we start off from an initial state
-> Each action will move the state from one to another
-> Some final state where we reach our goal

-> As a result, let us first clarify the clarify the initial



Its the same as LC solution with a change on class variable

'''

class Solution:
    
    found = 0
    
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        # Define Start Row, Col
        # Non obstacles to
        non_obstacles = 0
        start_row, start_col = 0,0
        
        for row in range(0, rows):
            for col in range(0,cols):
                cell = grid[row][col]
                if cell >= 0:
                    non_obstacles += 1
                if cell == 1:
                    start_row, start_col = row, col
                    
                
                
        
        def backtrack(row, col, remain):
            
            # Base case end
            if grid[row][col] == 2 and remain == 1:
                self.found += 1
                return

            # Mark visited
            temp = grid[row][col] 
            grid[row][col] = -4
            remain -= 1   # we now have one less square to visit

            # explore the 4 potential directions around
            for ro, co in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_row, next_col = row + ro, col + co

                if not (0 <= next_row < rows and 0 <= next_col < cols):
                    # invalid coordinate
                    continue
                if grid[next_row][next_col] < 0:
                    # either obstacle or visited square
                    continue

                backtrack(next_row, next_col, remain)

            # unmark the square after the visit
            grid[row][col] = temp
            
            
        backtrack(start_row, start_col, non_obstacles)

        return self.found