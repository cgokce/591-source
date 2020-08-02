'''
Design HashSet

It'll be linked list based hashing
Duplicate control is applied while traversing
Time: Best case O(1), worst case O(n), avg depends on m and n, should be close to O(m/n) for a balanced data and m>n
Memory m+n => O(max(m,n))

'''

class MyHashSet(object):

     # Standard linked root node
    class Node(object):

        next = None
        val = None

        def __init__(self, val):
            self.next = None
            self.val = val
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        # Number of operations to 10k
        # So lets use array with 10k memory
        self.set_size = 10000
        self.hash_set = [None for i in range(self.set_size)]
    
    def hash_func(self, val):
        # Basic hash function, index function
        return val % self.set_size
        
    def print_arr(self):
        out = ""
        for i in range(5):
            res = self.hash_set[i]
    
            if res is not None:
                out += str(res.val)
                temp = res
                while temp.next is not None:
                    out += "->" + str(temp.next.val)
                    temp = temp.next
            else:
                out += str(res)
        print("--- " + out + " ---")
    
    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        #print("add " + str(key))
        
        val = key
        index = self.hash_func(val)
        exists = False
        
        #print(index, val)
        
        # First if slot is None
        root = self.hash_set[index] 
        new_node = self.Node(val)
        if root is None:
            self.hash_set[index] = new_node
        else:
            
            if root.val == val:
                exists = True
            
            #Begin traversing
            while(root.next is not None):
                if root.next.val == val:
                    exists = True
                    break
                root = root.next
                
            #Add if not previously exists
            if not exists:
                root.next = new_node
        
        #self.print_arr()

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        
        #print("remove " + str(key))
        
        # Traverse, delete, change node pointer
        val = key
        exists = False
        index = self.hash_func(val)
        root = self.hash_set[index] 
        
        # Exists at the beginning, delete it
        if (root is not None):
            if root.val == val:
                exists = True
                next_node = root.next
                self.hash_set[index] = next_node
                #del root
            else:
                # Exists in the middle
                # This needs update
                
                while(root.next is not None):
                    next_node = root.next
                
                    if next_node.val == val:
                        exists = True
                        root.next = next_node.next
                        #del next_node
                        break
                    root = root.next
                
                '''
                while(root.next is not None):
                    if root.val == val:
                        exists = True
                        next_node = root.next
                        self.hash_set[index] = next_node
                        del root
                        # If it is the final node, previous->next to next->next
                        break
                    root = root.next
                '''
        
        # Not exists, do nothing
        #self.print_arr()
        

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        val = key
        exists = False
        index = self.hash_func(val)
        root = self.hash_set[index] 
        
        
        if (root is not None):
            if root.val == val:
                exists = True
            else:
                while(root.next is not None):
                    if root.next.val == val:
                        exists = True
                        break
                    root = root.next

        return exists
        
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

'''
Unit test
obj = MyHashSet()
obj.add(1)
obj.add(1)
obj.add(1)
obj.add(10001)
obj.remove(1)
obj.add(20001)
obj.add(1)
obj.add(1)
obj.add(30001)
obj.add(1)
obj.remove(1)
obj.add(2)
obj.add(3)
obj.remove(1)
obj.remove(10001)
for i in range(5):
    print(obj.contains(i))
'''
    
'''output with a problem

add 1
--- None1NoneNoneNone ---
add 1
--- None1NoneNoneNone ---
add 1
--- None1NoneNoneNone ---
add 10001
--- None1->10001NoneNoneNone ---
remove 1
--- None10001NoneNoneNone ---
add 20001
--- None10001->20001NoneNoneNone ---
add 1
--- None10001->20001->1NoneNoneNone ---

## FIX
add 1
--- None10001->20001->1->1NoneNoneNone ---
add 30001
--- None10001->20001->1->1->30001NoneNoneNone ---
add 1
--- None10001->20001->1->1->30001NoneNoneNone ---
remove 1
--- None10001->20001->1->30001NoneNoneNone ---
add 2
--- None10001->20001->1->300012NoneNone ---
add 3
--- None10001->20001->1->3000123None ---
remove 1
--- None10001->20001->3000123None ---
remove 10001
--- None20001->3000123None ---

'''
    