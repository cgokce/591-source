#### Wrapper Classes In Java

    https://www.baeldung.com/java-wrapper-classes

Wrapper Classes
- Objects encapsulating primitive Java types
- Each primitive has a corresponding wrapper
    - boolean, byte, short, char     , int    , long, float, double
    - Boolean, Byte, Short, Character, Integer, Long, Float, Double
- These all defined in java.lang package, there is no need to import
- Generic classes only work with objects and don't support primitives
    - Thus, if we want to work with them, we need to convert primitives to wrappers
    - Eg. Java Collection framework works with objects exclusively


Properties
- **Autoboxing**: we can write as ArrayList.add(101)
    - Java converts the primitive value to an Integer before storing it in the ArrayList using valueOf()
    - Automatic conversion that the Java compiler makes between the primitive types and corresponding object wrapper
        - Boxing -> Primitive value into a wrapper. Which happens automatically, its called auto boxing
        - Unboxing -> When wrapper object is unwrapped into a primitivie value
    - If we write a method accepts a primitivie value or wrapper objects, we can still pass both values to them
        - Java will take care of passing the right type eg. primitive or wrapper, we can pass both values to them
    - https://stackoverflow.com/questions/28897524/foreach-loop-by-primitive-or-by-boxed-class-in-java
- Converting Primitive to Wrapper Class
    - Using static factory methods:   //(or Constructor deprecated with Java9)
    
            Integer anotherObject = Integer.valueOf(1);

    - Returns cached values which makes it efficient
        - It always caches values between -128 to 127.
    - Converting wrapper object to primitive value
        - Use corresponding method such as intValue(), doubleValue() etc.
                int val = object.intValue();
