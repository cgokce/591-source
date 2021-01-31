#### Java Get Random Element from a List

    https://www.baeldung.com/java-random-list-element

Picking a Random Item
- You need to generate a random index then fetch an item by index 
- Get Random Item

        List<Integer> givenList = Arrays.asList(1,2,3);
        Random rand = new Random();
        int randomElement = givenList.get(rand.nextInt(givenList.size()));

- In a Multithreaded Environment
    - Using single random instance might result in getting the same random value each process accessing the instance
    - We can generate new instance per thread using ThreadLocalRandom class

            int randomElementIndex = ThreadLocalRandom.current().nextInt(listSize) % givenList.size();

- Select random item with repetitions, just use loop to get multiple items
- Without repetitions, after selecting item remove the item from the list
- For other randomness you can use Collections.shuffle(list) to shuffle element items