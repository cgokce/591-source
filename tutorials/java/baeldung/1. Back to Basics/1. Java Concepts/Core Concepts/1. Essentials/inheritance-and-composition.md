#### Overview

- Inheritance and composition are cornerstones of objet-oriented programming (OOP).

Inheritance (Is a Relationship)
- Powerful yet overused and misused mechanism
    - Base class aka base type defines the state and behavior common for a given type
    - Lets the subclasses (a.k.a. subtypes) provide specialized versions of that state and behavior
- Naive example: A base class Person that defines the common fields and methods for a person
    - Subclass Carpenter provides additional fine grained method implementations
    - Carpenter is a Person

            public class Person { -- }

            public class Carpenter extends Person { -- }

    - Generate a unit test to verify that instances of the Waitress and Actress classes are also instances of Person

            @Test
            public void givenWaitressInstance_whenCheckedType_thenIsInstanceOfPerson(){
                assertThat (new Carpenter("Bob", "mail", 22)).isInstanceOf(Person.class);
            }
- In which use cases is inheritance the right approach to take?
    - If subtypes fulfill the "is-a" condition and mainly provide additive functionality further down the classes hierarchy
    - The subtypes inherit the base type's API (note sometimes this is undesirable and we prefer other composition, prefer comp whenever possible)

---

Inheritance in Design Patterns

**The Layer Supertype Pattern**
- We use inheritance to move common code to a base class (the supertype), on a per-layer basis.

        public class Entity {
            protected long id;
            ...
        }

        public class User extends Entity {
            // additional fields and methods
        }

**The Template Method Pattern**
- We can use a base class to define the invariant parts of an algorithm
    - Then implement the variant parts in the subclasses
    - Just use abstract class and implement the parts inside subclasses

---

#### Composition (Has-a Relationship)

- Another mechanism provided by OOP for reusing implementation
- Composition allows us to model objects that are made up of other objects
- Composition is the strongest form of association
    - Objects that compose or are contained by one object are destroyed too when that object is destroyed


- Eg. Let's suppose that we need to work with objects that represent computers
- Computer is composed of different parts including the microprocessor

        public class Computer {

            private Processor processor;
            private GraphicsCard graphicsCard;
            private Memory memory;
        }

        public class Nvidia1080TI implements GraphicsCard { ... }
        public class AMDRyzen3700X implements Processor { ... }
        public class Kingston3200HZ1_16GB_CL14Memory implements Memory { ... }

- It is easy to understand the motivations behind pushing composition over inheritance.
    - Establishing semantically correct "has-a" relationship.
- We say Computer object has ownership of the contained objects
    - ONLY F objects can't be reused within another Computer object
    - If they can we'd be using aggregation, where ownership isn't implied

---

Composition Without Abstraction
- We could have defined composition relationship by hard-coding the dependencies of the Computer Class
        
        private Nvidia1080TI graphicsCard = new Nvidia1080TI()
        private AMDRyzen3700X processor = new AMDRyzen3700x()
- Of course this would be a rigid, thightly-coupled design
    - We can't take advantages of level of abstraction provided by interfaces and dependency injection (DI)
    - Computer strongly dependent on specific implementations of Processor and GraphicCard
- With the initial design based on interfaces we get a loosely coupled design, which is also easier to test