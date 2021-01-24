#### Comparing Long Values in Java

    https://www.baeldung.com/java-compare-long-values

Problems using Reference Comparion
- Long is a wrapper class for the primitive type long
- We need to compare the content of Long instances using .equals() instead of reference comparion
    - If we use == we can only compare -128 to 127, since java maintains constant pool for instances of small Longs
- In the general case two boxed instances having the same primitive value don't yield the same object reference

Comparison
- .equals() 
    - This will evaluate the content of both objects
            Long l1 = 128L;
            ...

            assertThat(l1.equals(l2)).isTrue();
- Object.equals()
    - This is a null-safe utility method

            Long l1 = null;
            Long l2 = 128L;

            assertThatCode(() -> Objects.equals(l1,l2)).doesNotThrowAnyException();


Unboxing Long Values
- Note: For these methods, we should check if the object is null, if so we'll get NullPointerException
- Using .longValue() Method

        assertThat(l1.longValue() == l2.longValue()).isTrue();

- Casting to primitive Values

        assertThat((long) l1 == (long) l2).isTrue();



