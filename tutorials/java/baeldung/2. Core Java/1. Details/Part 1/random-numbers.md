#### Random Numbers

    https://www.baeldung.com/java-generate-random-long-float-integer-double


Long
- Unbounded Long

        @Test
        public void givenUsingPlainJava_whenGeneratingRandomLongUnbounded_thenCorrect(){
            long generatedLong = new Random().nextLong();
        }
- Long within a Range
    - Plain Java

            long leftLimit = 1L;
            long rightLimit = 10L;
            long generatedLong = leftlimit + (long) (Math.random() * (rightLimit - leftLimit))

    - Using Apache Commons

            long generatedLong = new RandomDataGenerator().nextLong(leftLimit, rightLimit);

Integer
    - Unbounded

            int generatedInteger = new Random().nextInt();

    - Within a range
        - Plain Java

                int generatedInteger = leftLimit + (int) (new Random().nextFloat() * (rightLimit - leftLimit))
        
        - Commons

                int generatedInteger = new RandomDataGenerator().nextInt(leftLimit, rightLimit);

Float 
    - Unbounded

            float generatedFloat = new Random().nextFloat();
    
    - Within a range
        - Plain Java

                float generatedFloat = leftLimit + (float) (new Random().nextFloat() * (rightLimit - leftLimit));

        - Apache Commons

                float generatedFloat = new RandomDataGenerator().nextFloat(leftLimit, rightLimit);

Double
    - Unbounded
        - Plain Java
    
                double generatedDouble = Math.random();
        - Apache Commons

                double generatedDouble = new RandomDataGenerator().getRandomGenerator().nextDouble();

    - Within a range
        - Plain Java

                double generatedDouble = leftLimit + new Random().nextDouble() * (rightLimit - leftLimit)

        - Apache Commons

                double generatedDouble = new RandomDataGenerator().nextUniform(leftLimit, rightLimit);
