#### Java copyOnWriteArrayList

    https://www.baeldung.com/java-copy-on-write-arraylist

- When we want to iterate over a list in a thread-safe way without an explicit synchronization

The API
- It has different api design for multithread safety
- When we are using any of the modify methods, the whole content of the CopyOnWriteArrayList is copied into the new internal copy
- We can iterate over the list in a safe way in concurrent environments
- Iterator: When we get iterator, it'll be backed up by the immutable snapshot of the content on the copyOnWriteArrayList
- Good for the use cases when we are iterating over the arraylist more then we are modifying it

Iteration
- Generate instance and iterate over it

        CopyOnWriteArrayList<Integer> numbers = new CopyOnWriteArrayList<>(new Integer[]{1,3,5,8});

        Iterator<Integer> iterator = numbers.iterator();
        numbers.add(10);
        
        // When we iterate over iterator, we won't see number 10, since prev state is snapshotted
        List<Integer> result = new LinkedList<>();
        iterator.forEachRemaining(result::add);

        assertThat(result).containsOnly(1, 3, 5, 8);

        // If we get one more iterator, we will get all the numbers

- Removing while iterating is not allowed, iterator is not permitted to use remove, it'l throw UnsupportedOperationException
