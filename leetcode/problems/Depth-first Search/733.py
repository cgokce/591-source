'''
Flood Fill
<T> Depth-First Search

image -> 2D array of integers, pixel value 0-65k


coord(sr, sc) representing the row or column start
    - "flood fill" the image

To perform a flood fill: consider the starting pixel.
                        + any pixel connected 4 directionally starting of the same color
                        + connected 4d to those pixels.
                        
 At the end, change all
 
 
Example:
1 [1] 1 
1 1 0
1 0 1

sr = 1
sc = 1
new_color = 2

step1
1 [2] 1 
1 1 0
1 0 1

step 2
2 [2] 2 
1 2 0
1 0 1

step 3
2 [2] 2 
2 2 0
1 0 1

step 4
2 [2] 2 
2 2 0
2 0 1

..done

output:
2 2 2 
2 2 0
2 0 1 

Start end pixel could be anywhere
Image values and newColor all gonna be integers


Solution

# Image is sent by reference
def dfs(image, sr, sc, newColor)
    # We do not need to handle edge cases since 0<=sr/sc<len(img)
    
    # if there's nothing to color on
    # return
    
    # Color that location
    image[sr][sc] = newColor
    
    # Color the neighbors
    # Row 
    if sr>0:
        a = sr-1
        b = sc
        if image[a][b] not in [0,newColor]:
            dfs(image,a,b,newColor)
    if sr<len(image)-1:
        a = sr +1
        b = sc
        if image[a][b] not in [0,newColor]:
            dfs(image,a,b,newColor)
    # Col
    if sc>0:
        a = sr
        b = sc-1
        if image[a][b] not in [0,newColor]:
            dfs(image,a,b,newColor)
    if sc<len(image[0])-1:
        a = sr
        b = sc +1
        if image[a][b] not in [0,newColor]:
            dfs(image,a,b,newColor)
    
    return image


'''

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        
        def dfs(image, sr, sc, newColor,firstColor):
            # We do not need to handle edge cases since 0<=sr/sc<len(img)

            # if there's nothing to color on
            # return
            if image[sr][sc] == newColor:
                return image
            
            # Color that location
            image[sr][sc] = newColor

            # Color the neighbors
            # Row 
            if sr>0:
                a = sr-1
                b = sc
                if image[a][b] == firstColor:
                    dfs(image,a,b,newColor,firstColor)
            if sr<len(image)-1:
                a = sr +1
                b = sc
                if image[a][b] == firstColor:
                    dfs(image,a,b,newColor,firstColor)
            # Col
            if sc>0:
                a = sr
                b = sc-1
                if image[a][b] == firstColor:
                    dfs(image,a,b,newColor,firstColor)
            if sc<len(image[0])-1:
                a = sr
                b = sc +1
                if image[a][b] == firstColor:
                    dfs(image,a,b,newColor,firstColor)

            return image
        
        
        if image == None or image == [] or image == [[]]:
            return image
        
        
        # Update, it only modifies the same color of starting pixel
        firstColor = image[sr][sc]
        
        return dfs(image, sr, sc, newColor, firstColor)
        
                
        