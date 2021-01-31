#### Converting Iterator to List

    https://www.baeldung.com/java-convert-iterator-to-list

- Following examples will use the iterator

        Iterator<Integer> iterator = Arrays.asList(1,2,3).iterator();

Conversion
- Using a while loop, common approach before the Java 8

        List<Integer> actualList = new ArrayList<Integer>();
        while(iterator.hasNext()){
            actualList.add(iterator.next());
        }

        assertThat(actualList, containsInAnyOrder(1,2,3));

- Using J8 Iterator.forEachRemaining() method to build a list

        List<Integer> actualList = new ArrayList<Integer>();
        iterator.forEachRemaining(actualList::add);

        assertThat(actualList, containsInAnyOrder(1,2,3));

- Using J8 Streams API

        // We first convert Iterator to the Iterable
        Iterable<Integer> iterable = () -> iterator;

        // Now we can use StreamSupports stream and collcet methods to build the List
        List<Integer> actualList = StreamSupport
            .stream(iterable.spliterator(), false)
            .collect(Collectors.toList);
        
        assertThat(actualList, containsInAnyOrder(1,2,3));

- Using Guava, provides options to generate both mutable and immutable lists

        List<Integer> actualListImmutable = ImmutableList.copyOf(iterator);
        List<Integer> actualListMutable = Lists.newArrayList(iterator);

- Using Apache Commons

        List<Integer> actualList = ıteratorUtils.toList(iterator);

        