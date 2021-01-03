#### Lambdas and Comparison

    https://www.baeldung.com/java-8-sort-lambda

- Lambda support in Java 8, and how to leverage it to write Comparator
- Define Simple Entity Class to use it later

        public class Human {
            private String name;
            private int age;
        }

Basic Sorting
- Sort without lambdas:
    - Generating an anonymous inner class for the Comparator used in the sort.

            // Example building new comparator with overridden methods
            new Comparator<Human>() {
                @Override
                public int compare(Human h1, Human h2){
                    return h1.getName().compareTo(h2.getName());
                }
            }

            // When we are sorting we can build object there 
            Collections.sort(humans, new Comparator<Human>() {
                @Override
                public int compare(Human h1, Human h2) {
                    return h1.getName().compareTo(h2.getName());
                }
            });

- Sort with Lambda Support:
    - We can now bypass the anonymous inner class and achieve the same result
    - With simple and functional semantics

            (final Human h1, final Human h2) -> h1.getName().compareTo(h2.getName());

            // Test the behavior just as before
            humans.sort(
                (Human h1, Human h2) -> h1.getName().compareTo(h2.getName())
            );

- Sort with No Type Definitions
    - We can further simplify the expression by not specifying the type definitions
        - Compiler is capable of inferreng these on its own

                (h1,h2) -> h1.getName().compareTo(h2.getName());

                humans.sort(
                    (h1, h2) -> h1.getName().compareTo(h2.getName)
                );

- Sort using Reference to Static Method
    - Perform the sort using a Lambda Expression with a reference to a static method
            
            public static int compareByNameThenAge(Human lhs, Human rhs){
                if (lhs.name.equals(rhs.name)){
                    return Integer.compare(lhs.age, rhs.age);
                } else {
                    return lhs.name.compareTo(rhs.name);
                }
            }

            // Now we're going to call the humans.sort method with reference
            humans.sort(Human::compareByNameThenAge);

- Sort Extracted Comparators
    - We can also avoid defining even the comparison logic itself by using an instance method reference and the Comparator.comparing method

            Collections.sort(
                humans, Comparator.comparing(Human::getName)
            );

- Reverse Sort
    - Helper method for reversing the comparator, we can make quick use of that to reverse our sort

            Comparator<Human> comparator = (h1, h2) -> h1.getName().compareTo(h2.getName());

            humans.sort(comparator.reversed());

- Sort with Multiple Conditions
    - We can write more complex expressions as well using the lambda syntax, eg first sort by name, then by age

            humans.sort( (lhs, rhs) -> {
                if (lhs.getName().equals(rhs.getName())){
                    return Integer.compare(lhs.getAge(), rhs.getAge());
                } else {
                    return lhs.getName().compareTo(rhs.getName());
                }
            });

- Sort with Multiple Conditions using Composition
    - Above example can also be implemented using composition support
    - We can chain together multiple comparators to build more complex comparison logic

            humans.sort(
                Comparator.comparing(Human::getName).thenComparing(Human::getAge)
            );

- Sort with Stream.sorted()
    - Sort can be done with natural ordering or ordering provided by a Comperator
        - sorted() - uses natural ordering, element class must implement comperable interface
        - sorted(Comparator<? super T> comparator) - uses based on Comparator instance ordering
    - Using natural ordering

            @Test
            public final void givenStreamNaturalOrdering_whenSortingEntitiesByName_thenCorrectlySorted() {
                List<String> letters = Lists.newArrayList("B", "A", "C");

                List<String> sortedLetters = letters.stream().sorted().collect(Collectors.toList());
                assertThat(sortedLetters.get(0), equalTo("A"));
            }

    - Using custom Comparator

            Comparator<Human> nameComparator = (h1, h2) -> h1.getName().compareTo(h2.getName());

            List<Human> sortedHumans = humans.stream().sorted(nameComparator).collect(CollectorsçtoList());

    - Using Comparator.comparing method

            List<Human> sortedHumans = humans.stream()
                .sorted(Comparator.comparing(Human::getName))
                .collect(Collectors.toList());
    
- Sort reverse with Stream.sorted()

    - First example sort reverse by previously used Comparator.reverseOrder()

            List<String> reverseSortedLetters = letters.stream()
                .sorted(Comparator.reverseOrder())
                .collect(Collector.toList());
            
    - Now we use sorted() method and a custom Comparator

            // Flip the h1 and h2 to achieve reversing
            Comparator<Human> reverseNameComparator = 
                (h1, h2) -> h2.getName().compareTo(h1.getName());

            List<String> reverseSortedLetters = letters.stream
                .sorted(reverseNameComparator)
                .collect(Collectors.toList());

    - Above example with Comparator.comparing() method

            List<Human> reverseSortedHumans = humans.stream()
                .sorted(Comparator.comparing(Human::getName, Comparator.reverseOrder()))
                .collect(Collectors.toList());

---

Null Values
- So far, we have implemented our Comparators in a way they can't sort collectors containing null values
    - If collection have at least one null element, sort method throws *NullPointerException*

            @Test(expected = NullPointerException.class) {
                public void givenANullElement_whenSortingEntitiesByName_thenThrowsNPE() {
                    List<Human> humans = Lists.newArrayList(null, new Human("Jack", 12));

                    humans.sort((h1,h2) -> h1.getName().compareTo(h2.getName());
                }
            }

    - Simplest solution is handle null values manually in Comparator implementation
        - We can push null elements towards the end of collection
        - We design comparator to make null is greater than non-null values, and equal to null values

            humans.sort( (h1, h2) -> {
                if (h1 == null){ return h2 == null ? 0 : 1}
                else if (h2 == null) {return -1}
                return h1.getName().compareTo(h2.getName());
            });
    
    - We can pass any Comparator that is not null-safe into the Comparator.nullsLast() method
        - Comparator.nullsFirst moves null elements towards the start of the collection
        - We can also use the decorators for more readability

            humans.sort(Comparator.nullsLast(Comparator.comparing(Human::getName)));
    

    