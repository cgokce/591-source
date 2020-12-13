'''
Check if it is a Straight Line
<T> Array

int [] coordinates
    - coordinates[i] = [x,y] where [x,y] represents the coordinate of a point
    - Check if these points make a straight line in the XY plane



'''
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        if len(coordinates) <= 2:
            return True
        
        xdiff = coordinates[1][0] - coordinates[0][0]
        ydiff = coordinates[1][1] - coordinates[0][1]
        
        
        for i in range(2, len(coordinates), 1):
            if (xdiff * (coordinates[i][1] - coordinates[0][1]) !=  ydiff * (coordinates[i][0] - coordinates[0][0])):
                return False
            
        return True
        