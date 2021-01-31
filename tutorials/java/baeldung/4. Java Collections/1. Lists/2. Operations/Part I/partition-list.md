#### Partition a List in Java

    https://www.baeldung.com/java-list-split

- Split a list into several sublists of a given size

Using Guava
- Partition a List

        List<Integer> intList = Lists.newArrayList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
        List<List<Integer>> subSets = Lists.partition(intList, 3);

        List<Integer> lastPartition = subSets.get(2);
        List<Integer> expectedLastPartition = Lists.<Integer> newArrayList(7,8);
        assertThat(subSets.size(), equalTo(3));
        assertThat(lastPartition, equalTo(expectedLastPartition));

- Partition a collection bu generating sublist views of original collection

        Collection<Integer> intCollection = Lists.newArrayList(1,2,3,4,5,6,7,8);
        Iterable<List<Integer>> subSets = Iterables.partition(intCollection, 3);

        List<Integer> firstPartition = subSets.iterator().next();
        List<Integer> expectedLastPartition = Lists.<Integer> newArrayList(1,2,3);

Apache Commons
- Partition the List

        List<List<Integer>> subSets = ListUtils.partition(intList, 3);

        List<Integer> lastPartition = subSets.get(2);
        List<Integer> expectedLastPartition = Lists.<Integer> newArrayList(7,8);

Java 8 Partition the List
- Collectors partitioningby 

        Map<Boolean, List<Integer>> groups =
            intList.stream().collect(Collectors.partitioningBy( s -> s > 6));
        List<List<Integer>> subSets = new ArrayList<List<Integer>>(groups.values());

- Collectors groupingby

        Map<Integer, List<Integer>> groups = 
            intList.stream().collect(Collectors.groupingBy( s -> (s - 1) / 3));
        List<List<Integer>> subSets = new ArrayList<List<Integer>>(groups.values());

- By seperator dividing also possible, first finding the location of seperator then dividing by it