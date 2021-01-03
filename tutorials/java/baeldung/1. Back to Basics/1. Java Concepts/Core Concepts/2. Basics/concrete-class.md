#### Concrete Class in Java

    https://www.baeldung.com/java-concrete-class

Concrete Class
- Class that we can generate an instance of, using the new keyword
- Full implementation of its blueprant. A concrete class is complete

        // All methods are implemented, concrete class
        public class Car(){
            public String honk(){
                return "beep!";
            }
        
            public String drive(){
                return "brrrrr";
            }
        }

        // Since all methods are implemented we can call new on it
        Car car = new Car();

- Example JDK Concrete Classes
    - HashMap, HashSet, ArrayList, LinkedList...

---


Abstraction
- Not all Java types implement all their methods, this flexibility called abstraction
- We can achieve abstraction using interfaces and abstract classes

Interface
- Blueprint for a class
- Collection of the unimplemented method signatures
        interface Driveable(){
            void honk();
            void drive();
        }
- We can not instantiate it with the new keyword

Abstract Class
- Is a class that has unimplemented methods (can have mixed too).

        public abstract class Vehicle{
            public abstract String honk();

            public String drive() {
                return "zoom";
            }
        }

- **Marked with keyword abstract**
- Since Vehicle has an unimplemented method, we can't use new keyword
- Some JDK Examples: AbstractMap, AbstractList

---

Concrete Classes
- All methods are implemented
- Whether inherited or not, so long as each method has an implementation, class is concrete
- All classes which are not abstract, we can call them concrete
- Concrete classes can be as simple direct implementation as our Car example earlier
    - They can also implement interfaces and extend abstract classes

            public class FancyCar extends Vehicle implements Driveable {
                public String honk(){
                    return "brrrrr";
                }
            }

            //Inherits implementation of drive() from vehicle, so it is concrete
            FancyCar car = new FancyCar();

- Note using abstract keyword
    - Using abstract method in concrete class, compile error
    - Using abstract keyword in class with an abstract method, compile error