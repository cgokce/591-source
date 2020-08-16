
Complexity
- Time complexity is usually O(n) or O(k*n), which is about the node size.
- Space complexity is related to hold stack size, which is maximum depth * previously visited nodes, still goes O(n) usually
https://stackoverflow.com/questions/36479640/time-space-complexity-of-depth-first-search

Implementation Notes Using Python
- List or the nested lists always passed by the reference
- Otherwise it's possible to use .copy() on list to send a copy to next call (pass by value)
- You can also have a global variable to get rid of some backtracking, it saves time