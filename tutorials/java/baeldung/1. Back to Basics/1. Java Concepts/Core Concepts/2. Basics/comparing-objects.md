#### Introduction

    https://www.baeldung.com/java-comparing-objects

- Comparing objects is an essential feature of object-oriented programming languages.

== and != Operators
- Primitives
    - Being same means having the same values:

            assertThat(1 == 1).isTrue();
    - It also works when compparing with wrapper type thanks to autoboxing

            Integer a = new Integer(1);
            assertThat(l=a).isTrue();

Objects
- Summary: Objects compare addresses, values compare directly
- Let's say we want to compare two Integer wrapper types with the same value:

        Integer a = new Integer(1);
        Integer b = new Integer(1);

        assertThat(a == b).isFalse();
        
    - It **compares memory addresses in the stack that are different**
    - If we compare values we can they are same
        - Using valueOf() method that stores the Integer in cache
        - Too avoiding generating too many wraper objects with the same value
        - Method returns the same Integer instance for both calls

                Integer a = Integer.valueOf(1);
                Integer b = Integer.valueOf(1);
                
                assertThat(a == b).isTrue();
- Standard strings can also compare, but objects will not be comparable

                assertThat("Hello" == "Hello").isTrue(); // True
- Null References have similar behavior
    - Two null references are considered to be the same
    - Any non-null object will be considered different from null

        assertThat(null == null).isTrue();
        assertThat("Hello!" == null).isFalse();

- Behavior of equality operators, can be limiting
    - How we can compare two two objects have different address but same as internal states?


Object Instance.equals() Method
- Defined in the Object class so that every Java object inherits it
- By default its implementation compares object memory addresses
    - It works the same as the == operator
    - We can override this method in order to define what equality means for our objects
- Compare by object internal state
    - We can override the equals method to compare two classes based on their internal state

            public class Person{
                private String fileName;
                private String lastName;

                @Override
                public boolean equals(Object o){
                    if (this == 0) return true; //simply address check
                    if (o == null || getClass() != o.getClass()) return false;
                    Person that = (Person) p; // Convert to work for derived classes too
                    return firstName.equals(thatfirstName) && 
                        lastName.equals(that.lastName);
                }
            }

- It compares the value for existing objects eg. Integer

        Integer a = new Integer(1);
        Integer b = new Integer(1);

        assertThat(a.equals(b)).isTrue();

Object.equals() Static Method
- We can't use null as the value of the first object otherwise a NullPointerException would be thrown
- Equals() method of the **Objects helper class solves that problems**
    - It takes two arguments and compares them, also handling null values
- Compare person objects with the static comparison operator
    - Method already handles the null values

        Person john = new Person("John", "Doe");
        Person johnAgain = new Person("John", "Doe");
        Person arno = new Person("Arno", "Dorian");

        assertThat(Object.equals(john, johnAgain)).isTrue();
        assertThat(Object.equals(john, arno)).isFalse();

- Since object equals method handles null values, our implementation of .equals() method is much cleaner

        @Override
        public boolean equals(Object o){
            ...
            // Previous null checking version, unnecessary
            // birthDate == null ? that.birthDate == null : birthDate.equals(that.birthDate);

            // Static method handles the null checking for us
            Object.equals(birthDate, that.birthDate);

---

Comparable Interfaces
- Comparison logic can also be used to place objects in a specific order
- **Comparable** interface allows us to define an ordering between objects
    - Determine if object is greater, equal or lesser than another
- Comparable interface is generic and has only one method
    - .compareTo() -> Takes and argument of the generic type and returns an int
    - Returned Value:
        - Negative: Lower than the argument 
        - Zero: Two arguments are equal
        - Positive: Higher than the argument
- Eg. Person Class comparable using person's last name

        public class Person implements Comparable<Person>{
            ...

            @Override
            public int compareTo(Person o) {
                return this.lastName.compareTo(o.lastName);
            }
        }


Comparator Interface
- Simialar but seperated from the definition of the class
    - **We can define as many Comparators we want for a class**
- Generic and has a compare method that takes two arguments of that generic type
    - Returns an integer
- Eg. We also sort the people with their first names
    - We can use copmarator without changing previous class

            Comparator<Person> compareByFirstNames = Comparator.comparing(Person::getFirstName);

            Person john = new Person("John", "Doe");
            Person arno = new Person("Arno", "Dorian");

            List<Person> people = new ArrayList<>();
            people.add(john);
            people.add(arno);

            people.sort(compareByFirstNames);
            assertThat(people).containsExactly(arno,john);

- Other methods on Comparator interface we can use in our compareTo() implementation
    - Eg comparing last names, then first names, then birth dates (since birth rates are nullable we must tell how to handle)

        @Override
        public int compareTo(Person o){
            return Comparator.comparing(Person::getLastName)
                .thenComparing(Person::getFirstName)
                .thenComparing(Person::getBirthDate, Comparator.nullsLast(Comparator.naturalOrder()))
                .compare(this, o);
        }

---

Apache Commons Library
- org.apache.commons -> commons-lang3

ObjectUtils
- notEquals()
    - Takes two Object arguments to determine if they are not eual according to their own equals
            
            String a = new String("Hello!");
            String b = new String("Hello World!");

            assertThat(ObjectUtils.notEqual(a,b)).isTrue();
    - It is same as reverse of Object.equals()
- compare()
    - It is a generic method takes two Comparable arguments of that generic type
        - Returns an integer
        - Handles null values by considering them as greater

                assertThat(ObjectUtils.compare(a,b)).isNegative();

---

Guava
- com.google.guava -> guava

Objects
- equal()
    - Similar to commons, Google provides method to determine if objects are equal
    - With different implementations, they will return same results
- compare()
    - Only used to compare primitives

            assertThat(Ints.compare(1,2)).isNegative();
- ComparisonChainClass
    - Compare two objects through a chain of comparisons

            int comparisonResult = ComparisonChain.start()
                .compare(john.getLastName(), arno.getLastName())
                .compare(john.getFirstName(), arno.getFirstName())
                .result();
    
            assertThat(comparisonResult).isPositive();
    