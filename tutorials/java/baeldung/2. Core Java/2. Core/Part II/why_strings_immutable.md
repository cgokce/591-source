#### Why Strings Immutable?

- Strings are immutable but why
    - Java writer once told: I would use an immutable whenever I can
- Immutability features: caching, security, synchronization, performance, easy reuse without replication...

Immutable Object
- Object whose internal state remains constant after it has been entirely generated
    - Once assigned to a variable, we can not change it

String pool
- Caching the String literals and reusing them saves a lot of heap space
    - Different String variables refer to the same object in the String pool
    - Optimized by storing a single copy of each literal in the pool, called interning
- String Pool: Special memory region where String are stored by the JVM

        String s1 = "hey";
        String s2 = "hey";

        // They reference same object in the String Pool at heap space
        assertThat(s1 == s2).isTrue();

Security
- Strings often store sensitive pieces of information like usernames passowrds, connection URls etc.
- Example usage string on execution of db sql command
    - If Strings were mutable, we can't be sure that the String we received, even after performing security checks, would be safe
    - Untrustworthy caller method still has reference and can change String between integrity checks
    - Thus making our query prone to SQL injections
    - Immutability comes to rescue as it's easier to operate with sensitive code when values don't change, few interleaving operations

Synchronization
- Being immutable makes String thread safe, because it won't be changed when accessed from multiple threads
- Immutable objects in general, can be shared across multiple threads and thread-safe

Hashcode Caching
- String objects are widely used in hash implementations like HashMap, HashTable, HashSet etc.
- When operating upon these hash implementations hashCode() method is called frequently for bucketing
- hashCode() method overridden in String class to facilitate caching, such that 
    - The hash is calculated and cached during the first hashCode() call and same value returned ever since
    - So, it improves the performance of collections that uses hash implementations when operated with String object

Performance
- String pool exists since strings are immutable, thus enchances performance by saving heap memory, and faster hash implementations

Conclusion
- String references can be treated as a normal variable and one can pass them around, within methods and threads, without worrying about change