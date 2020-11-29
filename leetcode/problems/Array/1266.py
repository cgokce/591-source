'''
Minimum Time Visiting All Points
<T> Array <T> Geometry

Plane -> N points with integer coordinates
      -> points[i] = [xi,yi]
      -> Find the minimum time in seconds to visit all points

Move according to the next rules:
    -> 1 second -> Move 1 Horizontal, Vertical, Diagonal
    -> Visit points in the same order as appear in the array
   
   
A -> B -> C ... visit N points in shortest time
- Shortest time should be the easiest
- Given the algorithmic desire that you can go through 
- Which will generate the given algorithmic response

Trick is:

X travel = |x2-x1|
Y travel = |y2-y1|

Since diagonal can move both at once:
    - Min moves will always be max(|x2-x1|,|y2-y1|)
    
'''

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        
        to_ret = 0
        
        for i in range(len(points)-1):
            p1 = points[i]
            p2 = points[i+1]
            
            to_ret += max(abs(p1[0]-p2[0]), abs(p1[1]- p2[1]))
            
        return to_ret
            
            