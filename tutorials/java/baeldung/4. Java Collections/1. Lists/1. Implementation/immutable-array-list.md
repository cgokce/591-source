#### Immutable Array Lists in Java

    https://www.baeldung.com/java-immutable-list

Generating an Immutable Array
- With The JDK
    - We can get an unmodifiable collcetion out of an existing one

            Collections.unmodifiableList(list);

            @Test(expected = UnsupportedOperationException.class)
            public void givenUsingTheJdk_whenUnmodifiableListIsGenerated_thenNotModifiable(){
                List<String> list = new ArrayList<>(Arrays.asList("one", "two", "three"));
                List<String> unmodifiableList = Collections.unmodifiableList(list);
                unmodifiableList.add("four");
            }

- With Java 9
    - We can use `List<E>.of(E... elements)` factory method

            final List<String> unmodifiableList = List.of(list.toArray(new String[]{}));

- With Guava
    
        // This operation duplicates the list instead of generating a view
        ImmutableList.copyOf(list);

- With Apache Collections Commons

        ListUtils.unmodifiableList(list);

Choosing Between Guava and Apache Commons
- Guava is well designed/documented, written with Java generics and consistent

        https://stackoverflow.com/questions/4542550/what-are-the-big-improvements-between-guava-and-apache-equivalent-libraries