#### Remove Duplicates from a List

    https://www.baeldung.com/java-remove-duplicates-from-list

Remove Duplicates
- Using plain java, simply convert to the hashset

        List<Integer> listWithDuplicates = Lists.newArrayList(0,1,2,3,0,0);
        List<Integer> listWithoutDuplicates = new ArrayList<>(
            new HashSet<>(listWithDuplicates));

- Using guava

        List<Integer> listWithoutDuplicates
            = Lists.newArrayList(Sets.newHashSet(listWithDuplicates));
        
- Remove Duplicates from a list using J8 Lambdas, with distinct() method from stream api

        List<Integer> listWithoutDuplicates = listWithDuplicates.stream()
            .distinct()
            .collect(Collectors.toList());
