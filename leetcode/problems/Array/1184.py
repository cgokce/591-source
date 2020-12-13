'''
Distance Between Bus Stops
<T> Array


int [n] distance

bus has n stops
- 0 to n-1
- form a circle
- Distance between all pairs distance i is distance between
    - i , i+1
    
Give shortest direction between 2 stops
- CW or CCW

'''
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        
        found = False
        
        # calc cw
        cw = 0
        s = start
        found = False
        while not found:
            
            cw += distance[s]
            print(s, cw)
            if s == len(distance)-1:
                s = 0
            else:
                s+= 1
            

                
            if s == destination:
                found = True
                
        
        print("------")
        
        ccw = 0
        s = start
        found = False
        while not found:
            
            print(s, ccw)
            
            if s == 0:
                s = len(distance)-1
            else:
                s-= 1
            
            ccw += distance[s]
            if s == destination:
                found = True
        
        return min(cw, ccw)