'''
Available Captures for Rook
<T> Array

8x8 Chessboard -> 1 White Rook ('R')
               -> Empty Space (' ')
               -> White Bishops ('B')
               -> Black Pawn ('p')

Rook Moves: horizontal or vertical until decides to stop
    - or reaches at the edge
    - or capture opposite colored pawn
    
- Return number of pawns the rook can capture in one move
    - Check diagonals of rook
    - Will brute force
    
'''

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        

        def checkCount(row):

            ret = 0
            capture = False

            # Forward
            for i in range(len(row)):
                item = row[i]
                if item == 'p':
                    capture = True
                elif item == 'B':
                    capture = False
                elif item =='R':
                    break

            if capture:
                ret += 1
            capture = False

            # Reverse
            for i in range(len(row)-1, -1, -1):
                item = row[i]
                if item == 'p':
                    capture = True
                elif item == 'B':
                    capture = False
                elif item =='R':
                    break


            if capture:
                ret += 1
            return ret

        r,c = 0,0
        # Find the Rook
        for i in range(len(board)):
            row = board[i]
            for j in range(len(row)):
                item = board[i][j]

                if item == 'R':
                    r,c = i,j
                    break

        #print(r,c)

        ret = 0
        # Check row
        row = board[r]
        #print(row)
        ret += checkCount(row)
        #print(ret)
        
        
        
        # Transpose matrix, check column
        board_reversed = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))] 
        row = board_reversed[c]
        #print(row)
        ret += checkCount(row)
        
        
        return ret
        

            
            
        
        
        
                
                
                