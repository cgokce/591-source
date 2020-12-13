'''
Pascal's Triangle
<T> Array


int numRows, positive



'''
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        
        ret = []
        
        ret.append([1])
        ret.append([1,1])
        
        curr_row = []
        
        for i in range(2, numRows, 1):
            curr_row = [1]
            #print(i)
            #print(ret)
            
            for j in range(len(ret[i-1])-1):
                curr_row.append(ret[i-1][j] + ret[i-1][j+1])
            
            curr_row.append(1)
            ret.append(curr_row)
        
        return ret
            