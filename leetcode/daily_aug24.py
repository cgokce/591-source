'''
# DAG - All paths from source to target
we can apply a recursion through the 1-->n

Constraints
---> Empty list means there is no path from n, it is a sink node
---> Can return the order arbitrarily, no constraint on visiting
---> No cycles means no post elimination on the traverse results, it won't repeat


# Algorithm
--- Naive approach builds up the results with the recursion(dfs)

self.path_list = []

# Time complexity similar to O(max(n,v))
# Space complexity should be about O(n^2)
def algorithm(self, prefix, curr=0, graph):
    
    # Base case, when final node reached, return one list to be included in the final list
    if curr == len(graph)-1:
        prefix.append(curr)
        path_list.append(prefix)
        return
    
    # Recursion
    for i in len(graph[curr]):
        to_traverse = graph[curr][i]
        temp_prefix = prefix.append(3)
        return algorithm(self, temp, to_traverse, graph)
    
    return

'''



class Solution(object):
    
    path_list = []
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        self.path_list = []
        prefix = []
        curr = 0
        self.dfs(prefix, curr, graph)
        #print(self.printable(self.path_list))
        return self.path_list
    
    def printable(self, graph):
        out = ""
        for i in range(len(graph)):
            out += str(graph[i])
        return out
        
    def dfs(self, prefix, curr, graph):
        '''
        out = ""
        out += str(prefix) + str(curr) + self.printable(graph)
        print(out)
        '''
        prefix.append(curr)
        # Base case, when final node reached, return one list to be included in the final list
        if curr == len(graph)-1:
            print("adding" + str(prefix))
            self.path_list.append(prefix)
            return True

        # Recursion
        for i in range(len(graph[curr])):
            to_traverse = graph[curr][i]
            self.dfs(prefix[:], to_traverse, graph)
            #prefix.pop()
        
        return
        
        