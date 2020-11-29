'''
Ordered Stream
<T> Array


/*
Design an Ordered Stream
<T> Array 

- There is a stream of n (id, value)
    - Arbitrary order
    - id: (1, n), unique
    - Design a stream that returns the values
    - Increasing order of their IDs by returning a chunk (list) of values after each insertion
    - Concatenation of all chunks should result in a list of the sorted values
- Implement OrderedStream Class
    - Constructor
    - insert -> inserts pair id,value into the strum
        - return largest possible chunk of currently inserted values that appear next in order

Stupid description and unclear question

'''


class OrderedStream:

    streamList = []
    ptr = 0
    
    def __init__(self, n: int):
    
        self.streamList = [None for i in range(n)]
        self.ptr = 0
    

    def insert(self, id: int, value: str) -> List[str]:
        
        to_ret = []
        self.streamList[id-1] = value
        
        while (self.ptr < len(self.streamList) and self.streamList[self.ptr] != None):
            to_ret.append(self.streamList[self.ptr])
            self.ptr += 1
            
        return to_ret
        
        

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)