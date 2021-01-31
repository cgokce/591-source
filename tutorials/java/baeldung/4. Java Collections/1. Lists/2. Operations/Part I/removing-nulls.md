#### Remove all null elements from a list

    https://www.baeldung.com/java-remove-nulls-from-list

Using Plain Java
- Following simple methods will modify the source list

        List<Integer> list = Lists.newArrayList(null, 1, null);
        // Remove single item in a while loop
        while(list.remove(null));

        // Using removeAll
        list.removeAll(Collections.singleton(null));

        assertThat(list, hasSize(1));

Google Guava
- Using a more functional approach using predicates

        Iterables.removeIf(list, Predicates.isNull());

        // You can generate a new filter list
        List<Integer> listWithoutNulls = Lists.newArrayList(
            Iterables.filter(list, Predicates.notNull()));
        
Apache Commons Collections
- Similar functional Style

        CollectionUtils.filter(list, PredicateUtils.notNullPredicate());

Using Java8 Lambdas
- Parallel filtering

        List<Integer> listWithoutNulls = list.parallelStream()
            .filter(Objects::nonNull)
            .collcet(Collectors.toList());
        
- Searial filtering

        List<Integer> listWithoutNulls = list.stream()
            .filter(Objects::nonNull)
            .collect(Collectors.toList());

