#### Final Keyword in Java

    https://www.baeldung.com/java-final

- Final keyword: When we need to set limitations on extensibility for variaous reasons

Final Classes
- Classes marked as final cannot be extended
    - Eg. string

            public class myExtendedString extends String {...}
            
            // Compiler error:
            // The type myExtendedString cannot subclass the final class String

- Consider situation if we can extend the String class, override any of its methods
    - Result of the operations over String objects will then become unpredictable
    - Since String is used everywhere it is confusing
- Objects of the final classes are still mutable

Final Methods
- Methods marked as final cannot be overridden
    - When we decide it shouldn't be overridden we do it
    - Eg. isAlive() method in Thread class is final

    ... public final void sound();

    public class BlackDog extends Dog{
        public void sound() {...}
    }

    // Compiler error:
    // Cannot override the final method from Dog
    // sound() method is final and can't be overridden
- If our constructor calls other methods, we should generally declare these method final for above reason

Final Variables
- Variables marked as final can't be reassigned. Once initialized, cannot be altered
- Final Primitive Values
    - Let's declare a primitive final variable i, then assign 1 to it

            final int i=1;
            i = 2;
            // Compile error
            // The final local variable i may already have been assigned
- Final Reference Variables
    - If we have a final reference variable we cant reasssign it
    - Object of itself is still mutable

    final Cat cat = new Cat();

    cat = cat2;  // ERROR: Compiler Error
    cat.setWeight(5); // This is ok

Final Fields
- Can be either constants or write-once fileds
- In naming conventions class constants should be uppercase with components seperated by underscore("_") characters:

        static final int MAX_WIDTH = 999;

- Any final field must be initialized before the constructor completes
- For static final fields we can initialize them
    - upon decleration, or in the static init block
- For instance final fields
    - upon decleration, instance initialized block, in the constructors

Final Arguments
- Final argument can't be changed inside a method

        public void methodWithFinalArguments(final int x){
            x = 1; // ERROR: Final local variable x cannot be assigned
        }