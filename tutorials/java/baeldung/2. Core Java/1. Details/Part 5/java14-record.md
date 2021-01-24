#### Java 14 Record Keyword

    https://www.baeldung.com/java-record-keyword

- Passing immutable data between object is most comon
    - Prior to J14, this required generation of a class with boilerplate fields and methods
    - With Java 14 we can use records to remedy these problems

Purpose
- Immutability ensures the validity of the data without synchronization
- To accomplish this, we generate data classes with following
    - private, final field for each piece of data
    - getter for each field
    - public constructor with a corresponding argument for each field
    - equals method that returns true for objects of the same class when all fields match
    - hashCode method returns the same value when all fields match
    - toString mathod
- This generates a lot of boilerplate code
- Update is non trivial, we need to update code when a new field is added
- Extra code obscures that our class is simply a data class

Record Basics
- We can replace our repetitious data classes with records
- Records are immutable data classes that require only the type and name of fields

        public record Person(String name, String address){}

- Constructor: Public constructor with an argument for each field is generated for use
- Getters: Public getters are also initialized
- equals(): Equals method is generated that returns true same type and values of all its field match
- hashCode(): Returns same value for two Person objects if all the field match 
    - Careful with collisions due to the birthday paradox
- toString(): automatically generated

Constructors
- We can still customize our constructor implementation, should be kept simple as possible since intended to use for validation
    - Eg. we can check if not null

        public record Person(String name, String address) {
            public Person {
                Objects.requireNonNull(name);
                Objects.requireNonNull(address);
            }
        }
- As with class constructors, fields can be referenced using this keyword
- Generating a constructor with same argumnets are valid but requires to be manually initialized

        public record Person(String name, String address) {
            public Person(String name, String address){
                this.name = name;
                this.address = address;
            }
        }

- Declaring a no-argument constructor and one with an argument list matching the generated constructor, result in construction error

Static Variables & Methods
- We can also include static variables and methods in our records
- Declare static variables or static methods as the same syntax

        public record Person(String name, String address){
            public static String UNKNOWN_ADDRESS = "Unknown";
        }