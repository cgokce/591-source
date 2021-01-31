#### Java ArrayList

    https://www.baeldung.com/java-arraylist

- It is included in java core libraries as java.util.ArrayList;
- Built on the array, which dynamically grow and shirnk as you add/remove elements
- Elements can be accessed by teir indexes starting from zero
- Properties
    - Random access takes O(1) time
    - Adding element takes constant O(1)
    - Insert/Delete is O(n)
    - Search takes O(n) for unsorted, O(log N) for sorted arr

Using the ArrayList
- ArrayList is a generic class, you can parametrize it with any type you want
- Good practice to use generic interface List as a variable type
    - Decouples it from a particular implementation

Initialization
- Default no-arg constructor

        List<String> list = new ArrayList<>();
        assertTrue(list.isEmpty());

- Declaring lenght of list

        // Size of a 20
        List<String> list = new ArrayList<>(20);

- Initialize from a collection

        Collection<Integer> number = IntStream.range(0,10).boxed().collect(toSet());

        List<Integer> list = new ArrayList<>(numbers);
        assertEquals(10, list.size());
        assertTrue(numbers.containsAll(list));

Adding Elements
- Insert an element at the end or at the specific position

        List<long> list = new ArrayList<>();

        list.add(1L);   // Add elem to the end
        list.add(2L);
        list.add(1, 3L); // Add eleme to specific position

        assertThat(Arrays.asList(1L,2L,3L), equalTo(list));

Iterate over ArrayList
- Two iterators available
    - Iterator: Traverse the list in one direction
    - ListIterator: Traverse the list in both directions

            //List Iterator Example
            List<Integer> list = new ArrayListz<>(
                IntStream.range(0,10).boxed().collect(toCollection(ArrayList::new))
            );

            ListIterator<Integer> it = list.listIterator(list.size());
            List<Integer> result = new ArrayList<>()
            while (it.hasPrevious()){
                result.add(it.previous());
            }

            Collections.reverse(list);
            assertThat(result, equalTo(list));

Search the ArrayList
- Using a collection

        List<String> list = LongStream.range(0,16)
            .boxed()
            .map(Long::toHexString)
            .collect(toCollection(ArrayList::new))
        List<String> stringsToSearch = new ArrayList<>(list);
        stringsToSearch.addAll(list);

- Using indexOf() or lastIndexOf() methods

        assertEquals(10, stringsToSearch.indexOf("a"));

- You may filter collection using J8 Stream API using predicate

        Set<String> matchingStrings = new HashSet<>(Arrays.asList("a","c","9"));

        List<String> result = stringsToSearch
            .stream()
            .filter(matchingStrings::contains)
            .collect(toCollection(ArrayList::new));

        assertEquals(6, result.size());

- Searching a sorted list may be done with binary search which is faster than linear

        List<String> copy = new ArrayList<>(stringsToSearch);
        Collections.sort(copy);
        int index = Collections.binarySearch(copy, "f");
        assertThat(index, not(equalTo(-1)));

Remove Element from the ArrayList
- You should find its index and only then perform the removal via remove() method
- Overloaded version of this method accepts an object, searches for it and performs removal of the first occurance

        List<Integer> list = new ArrayList<>(
            IntStream.range(0,10).boxed().collect(toCollection(ArrayList::now))
        );
        Collections.reverse(list);

        // Removes by index
        list.remove(0);
        assertThat(list.get(0), equalTo(0));

        // Remove value since boxed type is provided
        list.remove(Integer.valueOf(0));
        assertFalse(list.contains(0));



