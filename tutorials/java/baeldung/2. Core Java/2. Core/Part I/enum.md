#### Enum Iteration in Java

    https://www.baeldung.com/java-enum-iteration

- Enum is a datatype helps us assign a predefined set of constant to a variable.
- Summary: When iterating enum Stream is good option when performing any parallel operations
    - Otherwise you might use any of the methods
- Let's define example Enum to use it later

        public enum DaysOfWeekEnum {
            SUNDAY,
            MONDAY,
            TUESDAY,
            WEDNESDAY,
            THURSDAY,
            FRIDAY,
            SATURDAY
        }

Iterating Enums
- For Loop Iteration
    - We can use the array of Enum values returned by the values() methods.  

            for (DaysOfWeekEnum day : DaysOfWeekEnum.values()){
                System.out.println(day);
            }

- Stream Iteration
    - To generate stream we have two options
    - Using Stream.of:

            Stream.of(DaysOfWeekEnum.values());
    
    - Using Arrays.stream

            Arrays.stream(DaysOfWeekEnum.values());

    - Extend the DaysOfWeekEnum class to generate an example using Stream:

            public enum DaysOfWeekEnum{
                
                SUNDAY("off");
                MONDAY("working");
                TUESDAY("working);
                ...


                private String typeOfDay;

                DaysOfWeekEnum(String typeOfDay){
                    this.typeOfDay = typeOfDay;
                }

                public static Stream<DaysOfWeekEnum> stream() {
                    return Stream.Of(DaysOfWeekEnum.values());
                }
            }

            // Now call the stream to print non-working days
            DaysOfWeekEnum.stream()
                .filter(d-> d.getTypeOfDay().equals("off"))
                .forEach(System.out::println);
    
- forEach() iteration via conversion
    - By default enums do not have methods for iteration like forEach() or iterator().
    - forEach() is added to Iterable interface in Java 8
    - All the java collection classes have implementations of a forEach() method
    - To use it with Enum, first convert it to suitable collection

            Arrays.asList(DaysOfWeekEnum.values())
                .forEach(day -> System.out.println(day));

- Iterate Using EnumSet
    - EnumSet is a specialized set implementation that we can use with Enum types

            EnumSet.allOf(DaysOfWeekEnum.class)
                .forEach(day -> System.out.prinln(day));

- Using an ArrayList of Enum Values
    - We can add values of an Enum to List, use it like any other

            List<DaysOfWeekEnum> days = new ArrayList<>();
            days.add(DaysOfWeekEnum.FRIDAY);
            ..

            for (DaysOfWeekEnum day : days){
                System.out.prinln(day);
            }

            // Arrays.asList() can be also used but it would be immutable
            List<DaysOfWeekEnum> days = Arrays.asList(DaysOfWeekEnum).values());
