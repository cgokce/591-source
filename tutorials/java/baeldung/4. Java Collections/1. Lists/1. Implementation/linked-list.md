#### Java LinkedList

    https://www.baeldung.com/java-linkedlist

- ArrayList is default list implementation but in some cases LinkedList is also used
- LinkedList is a doubly linked-list implementation of the List and Deque interfaces
- Implements all optional list opertaions and permits all elements (including null)

Features
- Operations that index into the list will traverse the list from the beginning or the end, whichever is closer to the specified index
- It is not synchronized
- Its Iterator and ListIterator iterators are fail-fast
    - After the iterator's generation if the list is modified a ConcurrentModificationException will be thrown
- Every element is a node, keeps a reference to the next and previous ones
- It maintains the insertion order

- Although LinkedList is not synchronized, we can retrieve synchornized version
    - Colllections.synchronizedList
    - List list = Collections.synchronizedList(new LinkedList(...));

---

Comparison to ArrayList

Structure
- ArrayList is an index based structure backed by an Array
    - Random access is O(1)
- LinkedList stores its data as a list of elements, every element is linked to prev and next element
    - Search operation execution time O(n)

Operations
- Insertion addition and removal operations of an item are faster in LinkedList
    - Because there is no need to resize

Memory Usage
- LinkedList: Consumes more memory than ArrayList because every node in a LinkedList stores two references
- ArrayList: Only holds data and its index

---

Code Examples
- Generate new object

        LinkedList<Object> linkedList = new LinkedList<>();

- Add element via add(), addAll()
- Add element to position via addFirst() and addLast()
- Remove element by removeFirst, removeLast(), removeFirstOccurence(), removeLastOccurence()
- Queue like operations are implemented eg. poll() and pop() and push()
    - For an empty list
        - poll returns null
        - pop throws NoSuchElementException
