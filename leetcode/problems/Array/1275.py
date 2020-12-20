'''
Find Winner on a Tic Tac Toe Game
<T> Array


int [3][3] grid

- Player take turns placing chars in empty square (" ")
- First player places X, second player places O
- Game ends when there are 3 of sma echaracyter filling any row, col or diag
    - Also ends when all squares not empty

int [] moves
- Each element is another array of size 2
    - Corresponding to the row and column of the grid
    - Mark their respective character in the order in which A and B play
    
- Return winner "A" or "B", or if game ends return Draw
    - if there are still movements to play, return "Pending"
- Moes is valid, the grid is initially empty and A will play first
'''
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        
        # If smaller than 4 moves, there is no winner
        if len(moves) >4:
            board = [[" " for i in range(3)] for j in range(3)]

            # Fill board
            for i in range(len(moves)):
                item = moves[i]
                if i%2 == 0:
                    player = "A"
                elif i%2 == 1:
                    player = "B"
                board[item[0]][item[1]] = player 
            
            # Print mat
            for row in board:
                rowp = ""
                for item in row:
                    rowp += item + " "
                print(rowp)
            
            
            # Check if one is winner
            
            # Rows
            for row in board:
                found = True
                for i in range(len(row)-1):
                    if row[i] == " " or row[i] != row[i+1]:
                        found = False
                        break
                if found:
                    print("found row", row)
                    return row[i]
        
            # Cols
            transposed = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))] 
            for row in transposed:
                found = True
                for i in range(len(row)-1):
                    if row[i] == " " or row[i] != row[i+1]:
                        found = False
                        break
                if found:
                    print("found col", row)
                    return row[i]
                
            # Diags
            if board[1][1] != " " and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
                print("found diag 1")
                return board[1][1]
            elif board[1][1] != " " and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
                print("found diag 2")
                return board[1][1]
            
        
        # If there is no winner
        if len(moves) == 9:
            return "Draw"
        else: 
            return "Pending"