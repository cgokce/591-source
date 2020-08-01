##########################################################
# CODE INSTRUCTIONS:                                     #
# 1) The method findLargestSmallerKey you're asked       #
#    to implement is located at line 30.                 #
# 2) Use the helper code below to implement it.          #
# 3) In a nutshell, the helper code allows you to        #
#    to build a Binary Search Tree.                      #
# 4) Jump to line 71 to see an example for how the       #
#    helper code is used to test findLargestSmallerKey.  #
##########################################################

'''
Constraints
- Find smallest largest key in the tree
- If such number does not exists, return -1
  - eg. For num = 4   +
  - eg. For an empty tree  +
  - eg. For a tree that has only the base node +
- Does the graph includes the num? False. +



Algorithm
Traverse tree, start with the root node 

if num < node:
  # Failure condition
  go left side
elif num > node:
  # Success condition
  hold_key = current_key
  go right side
  
-recursive approach
base condition is reaching a leaf node
- failure cases
check if starting node is empty, also return -1
check if the starting empty tree

Exc
20 -> is_leaf? return the 

17 20
go left
17 9
go right, hold 9
17 12 
go right, hold 12
17 14
go right, hold 14
leaf reached, return last leaf



# Time Complexity
- We are using the BST, access to element is O(logN)

# Memory Complexity
- We apply recurison for node<num at maximum of tree height, still constant O(1)


'''


# A node 
class Node:

# Constructor to create a new node
  def __init__(self, key):
      self.key = key
      self.left = None
      self.right = None
      self.parent = None

# A binary search tree 
class BinarySearchTree:

  # Constructor to create a new BST
  def __init__(self):
      self.root = None

  def find_largest_smaller_key(self, num):
    return self.dfs(self.root, num)
      
  
  def dfs(self, node, num):
    score = -1
    
    # Base case
    # Exc. empty tree
    if node is None:
      return -1
    else:
      print(node.key)
      # Traversion
      if num <= node.key:
        # Failure condition
        # Left turn
        score = self.dfs(node.left, num)
          
      elif num > node.key:
        # Success condition
        # Right turn
        score = node.key
        returned = self.dfs(node.right, num)
        if returned > score and returned < num:
          score = returned
          
    
    return score
  
  
  # Given a binary search tree and a number, inserts a
  # new node with the given number in the correct place
  # in the tree. Returns the new root pointer which the
  # caller should then use(the standard trick to avoid
  # using reference parameters)
  def insert(self, key):

      # 1) If tree is empty, create the root
      if (self.root is None):
          self.root = Node(key)
          return

      # 2) Otherwise, create a node with the key
      #    and traverse down the tree to find where to
      #    to insert the new node
      currentNode = self.root
      newNode = Node(key)

      while(currentNode is not None):
        if(key < currentNode.key):
          if(currentNode.left is None):
            currentNode.left = newNode
            newNode.parent = currentNode
            break
          else:
            currentNode = currentNode.left
        else:
          if(currentNode.right is None):
            currentNode.right = newNode
            newNode.parent = currentNode
            break
          else:
            currentNode = currentNode.right

######################################### 
# Driver program to test above function #
#########################################

bst  = BinarySearchTree()
 
# Create the tree given in the above diagram 
bst.insert(20)
bst.insert(9);
bst.insert(25);
bst.insert(5);
bst.insert(12);
bst.insert(11);  
bst.insert(14);    

result = bst.find_largest_smaller_key(17)
#result = bst.find_largest_smaller_key(20)
#result = bst.find_largest_smaller_key(21)


print ("Largest smaller number is %d " %(result))
