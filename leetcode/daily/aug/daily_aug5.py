'''

addWord(word)
search(word) --> can be literal word
             --> can be regular exp containing a to z, or .
             

# 1. Naive solution implemented with array, look at the 
O(m*n)  , m = size of the query string(except the dot)
This only works when len(word) == search(word)

Add is simple just word_list.append(query)

Search:

found = True

for item in word_list:
    found =True
    for i in len(query):
        c = query[i]
        c2 = item[i] 
        
        if c==".":
            continue
        else: 
            if c==c2:
                continue
            found = False
    if found:
        break

return found


# 2. Better approach LL based HashMap since it access with O(1), so would be effective
# Problem is string hashing function implementation, that is hard to come up

# 3. A tree would be good for such search operation, we can build a tree for tehea each char
# bad, dad, mad
# Maybe it should be bottom up since problem description is bottom up
b -> a -> d
d -> a -> d
m -> a -> d
# we can reverse the strings and reversely build the tree, still not an effective data structure
# Problem that we need to build an n-tree with char at node, not as effective.


# 4. A trie. That is an effective way to implement a data structure, that supports this regex like search
# It is a n-tree with each node consisting hashmap that can contain multiple chars
# It contains a single success flag each node that holds the termination condition

class TrieNode():
    map< char, TrieNode> map;
    bool terminate = False;
    
we'll use python dict for the hash_map


--> Analysis
Without regex, m=len(w), time complexity O(m), space comp O(m)
with regex, we eval root times * dict_size, about O(m*n) maybe worst case, space should be same m*n due to recursion


'''

class WordDictionary(object):

        
    # Linked List Node
    class TrieNode(object):
        
        hmap = {}
        isEnd = False
        
        # Defeault constr, create a new node
        def __init__(self):
            self.hmap = {}
            self.isEnd = False
            
        def containsKey(self,c):
            return (c in self.hmap)
        
        # Returns next node
        def get(self, c):
            return self.hmap[c]
        
        def put(self, c, next_node):
            self.hmap[c] = next_node
        
        def str_dict(self):
            out_text = ""
            for k in self.hmap.keys():
                out_text += k + " , "
            return "["+ out_text + "]"
            
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Init an empty root.
        self.root = self.TrieNode()
        
        
        
    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        
        node = self.root
        
        for c in word:
            if not node.containsKey(c):
                
                #print("Added", c ,"to node")
                next_node = self.TrieNode()
                node.put(c, next_node)
            
            node = node.get(c)
        
        node.isEnd = True
        
        
        '''
        # Recursive Operation
        self.dfs(self, self.root, word)
    
    def dfs(self, root, remaining):
        # Base Case, remaining is empty
        if remaining == "":
            return root.terminate
        
        
        # Create the nextNode
        next_node = TrieNode()
        
        # Use hashmap add current node
        
        
        
        # Recursion
        return self.dfs(next_node, remaining[1:])
        '''        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        
        # This is a standard Trie call
        '''
        node = self.searchPrefix(word)
        return (node != None) and (node.isEnd)
        '''
        
        # Regex variant with the dfs
        return self.dfs(self.root, word)
        
        
    def searchPrefix(self, word):
        
        
        node = self.root
        
        
        # Also add the regex like search here
        # "." is a joker char
        # For the "." we need to traverse all subtrees
        
        for c in word:
            
            if node.containsKey(c):
                node = node.get(c)
            else:
                return None
        
        return node
    
    def dfs(self, node, word):
        
        # Base case
        if word == "":
            if node.isEnd: #and node.hmap.keys() != []:
                #print("base case node ", node.str_dict(), "returnsTrue")
                return True
            else:
                return False
        '''
        for c in word:
            print(node.str_dict(), c , " in ", word)
            found = False
            #print(c)
            
            if c == '.':
                print("Found contains dot")
                for k in node.hmap.keys():
                    next_node = node.get(k)
                    # Dot can be any char (!we cannot skip the word)
                    found = found or self.dfs(next_node, word[1:])      
            elif node.containsKey(c):
                print("Found contains: ", c)
                next_node = node.get(c)
                found = found or self.dfs(next_node, word[1:])
            #else:
            #    print("Not found")
            
            if not found:
                print("Not found")
                return False
        '''
        
        c = word[0]
        #print(c)

        if c == '.':
            #print("Found contains dot")

            # This need to traversed no matter what
            for k in node.hmap.keys():
                next_node = node.get(k)
                # Dot can be any char (!we cannot skip the word)
                if self.dfs(next_node, word[1:]):
                    return True
            return False
        elif node.containsKey(c):
            #print("Found contains: ", c)
            next_node = node.get(c)
            return self.dfs(next_node, word[1:])
        else:
            #print("Not found")
            return False
        
        #return found
        
        

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

''' Failure Case
["WordDictionary","addWord","addWord","search","search","search","search","search","search"]
[[],["a"],["a"],["."],["a"],["aa"],["a"],[".a"],["a."]]
Output:
[null,null,null,true,true,true,true,true,true]
Expected:
[null,null,null,true,true,false,true,false,false]
'''
'''
obj = WordDictionary()
obj.addWord("a")
obj.addWord("a")
out_text = ""

for word in [".", "a", "aa", "a", ".a", "a."]:
    out_text += str(obj.search(word))
print(out_text)

#print(obj.search("aa"))
print("------\n\n\n")
'''

'''

["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
'''

'''
[addWord","addWord","addWord","addWord","search","search","addWord","search","search","search","search","search","search"]
[["at"],["and"],["an"],["add"],["a"],[".at"],["bat"],[".at"],["an."],["a.d."],["b."],["a.d"],["."]]


Output:
[null,null,null,null,false,false,null,false,true,false,false,true,false]
Expected:
[null,null,null,null,false,false,null,true,true,false,false,true,false]
'''
