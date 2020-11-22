'''
Find common characters
<T> HashTable

given: arr<lowercase letters> A
- return list of all characters that show up in all strings within the list.
if character occurs 3 times, you include it 3 times in answer


'''


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        
        
        def map2list(mymap):
            ret = []
            # Final hmap to list
            for k in mymap.keys():
                v = mymap[k]
                for i in range(v):
                    ret.append(k)
            return ret
        
        
        total_map = {}
        first = True
        
        
        ## Do for all words
        for word in A:
            
            ## Find curr map
            curr_map = {}
            for c in word:
                if c in curr_map:
                    curr_map[c] += 1
                else:
                    curr_map[c] = 1
                    
            #print(map2list(curr_map))
            #print("---")
            
            ## Merge with total map
            if first:
                total_map = curr_map.copy()
                first = False
            else:
                out_map = {}
                for k in curr_map.keys():
                    v = curr_map[k]
                    if k in total_map:
                        out_map[k] = min(total_map[k], curr_map[k])
                total_map = out_map.copy()
        
        
        ret = map2list(total_map)
        
        return ret
        