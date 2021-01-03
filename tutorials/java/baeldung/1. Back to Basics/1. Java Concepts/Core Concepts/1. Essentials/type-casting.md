#### Object Type-Casting in Java

- Two kinds of types
    - Primitives
    - References
- Refences casting discussed here

Primitive vs Reference Difference
- Primitive variable contains its value conversion of a primitive variable means irreversible changes in its value
- Reference variables are different
    - Reference variable only refers to an object but **doesn't contain** object itself
- Casting a reference variable doesn't touch the object it refers to but only labels this object in another way
    - Expanding and narrowing opportunities to work with it
    - Upcasting narrows the list of methods and properties available to object
    - Downcasting extend list of methods and props

---

- **Reference is like a remote control to an object**
    - Remote control has more or fewer buttons depending on its type
    - Object itself is stored in a heap
    - **When we do casting, we change the type of the remote control but we doesn't change the object itself**

- **Upcasting**
    - Casting from a subclass to a superclass is called upcasting
    - Closely related to inheritance
    - It is common to use reference variables to refer to a more specific type
    - Every time we do this, implicit upcasting takes place

            public class Animal {...eat()...}
            public class Cat extends Animal {...eat()...meow()...}

            // Generate new cat
            Cat cat = new Cat();

            // Upcasting
            Animal animal = cat;  //automatic, since computer knows Cat is an Animal there is no error
            animal = (Animal) cat;  //explicit

            // After upcasting we cant invoke the cat specific methods
            animal.meow()  
            // ERROR: The method meow() is undefined for the animal
            // To fix this we need to downcast animal
    - **Using upcasting, we can take advantage of polymorphism**

- **Polymorphism**
    - Defined another subclass of animal, Dog

            public class Animal {...eat()...}
            public class Cat extends Animal {...eat()...meow()...}
            public class Dog extends Animal {...eat()...}

    - Now we can define feed() method which treats all cats and dogs like animals

            public void feed(List<Animal> animals){
                animals.forEach(animal -> {
                    animal.eat();
                });
            }

            // Implicit upcasting occurs when we add animals into animals list

            List<Animal> animals = new ArrayList<>();
            animals.add(new Cat());
            animals.add(new Dog());
            new AnimalFeeder().feed(animals)

    - **All java objects are polymorphic because each object is an Object at least**
    - All Java objects we generate already have Object specific methods, eg toString
    
            // We can assign an instance of Animal to the reference variable of Object type
            Object object = new Animal();

    - Upcasting to an Interface is also common

            public interface Mew{... meow() ...}
            public class Cat extends Animal implements Mew{}

            // Now any Cat object can also be upcast to Mew
            // Cat is a Mew, upcasting is legal and done implicitly
            Mew mew = new Cat();

            // Cat is an Animal, Mew and Object and Cat. Can be assigned to any of them. 
- **Overriding**
    - In the example above the eat() method is overridden
    - Although eat() is called on variable on Animal type, work is done by methods invoked on real objects - cats and dogs
    
            public void feed(List<Animal> animals) {
                animals.forEach(animal ->) {
                    animal.eat();
                }
            };

            // We add debugging and see calls from subclasses
            // - cat is eating, dog is eating
    - **SUM UP**
        - Reference variable can refer to an object if the object is of the same type as a variable or if it is a subtype
        - Upcasting happens implicitly
        - All Java objects are polymorphic and can be treated as objects of supertype due to upcasting

--- 

- **Downcasting**
    - Use when we want to use the variable of type Animal to invoke a method available only to Cat class
    - Downcasting is casting from a superclass to a subclass

            Animal animal = new Cat();

            // To call meow() we should downcast to Animal, () is the cast operator
            ((Cat) animal).meow();

            animals.forEach(animal ->{
                animal.eat();
                if (animal instanceof Cat){
                    ((Cat) animal).meow()
                }
            }

            // Output: cat is eating, meow, dog is eating
            // We only downcasted the instances of Cat

    - **Instanceof Operator**
        - Often use operator before downcasting to check if the object belongs to the specific type
    - **ClassCastException**
        - If we hadn't checked type with the instanceof operator, compuler wouldn't have complained
        - At runtime there will be an exception, always cast to runtime
        - Above example: We would be trying to convert an object which is an instance of Dog into a Cat instance
        
    - Compile Downcast Error to Unrelated Type
        - **To compile, both types should be in the same inheritance tree**

                Animal animal;
                String s = (String) animal;
                // Compile error: Cannot cast from Animal to String
        
    - **SUM UP**
        - Downcasting is necessary to gain access to members specific to subclass()
        - Downcasting is done using cast operator
        - To downcast an object safely, we need instanceof operator
        - If the real object doesn't match the type we downcast to, then ClassCastException will be thrown at runtime
    
- **cast() Method**
    - Another way to cast objects using the methods of Class

            Animal animal = new Cat();
            if (Cat.class.isInstance(animal)) {
                Cat cat = Cat.class.cast(animal);
                cat.meow();
            }
    
    - Eg. Generic Class with feed() method which feeds only one type of animals, cats or dogs, depending on the value of the type parameter:

            public class AnimalFeederGeneric<T>{

                private Class<T> type;

                public AnimalFeederGeneric(Class<T> type) {
                    this.type = type;
                }

                public List<T> feed(List<Animal> animals) {
                    List<T> list = new ArrayList<T>();

                    animals.forEach(animal -> {
                        if (type.isInstance(animal)) {
                            T objAsType = type.cast(animal);
                            list.add(objAsType);
                        }
                    })

                }

            }

            // Feed method checks each animal and returns only those which are instances of T
            // Class instance should also be passed to the generic class as we can't get it from the type parameter T
            // In our example we pass it in the constructor

            // Usage
            List<Animal> animals = new ArrayList<>();
            animals.add(new Cat());
            animals.add(new Dog());
            AnimalFeederGeneric<Cat> catFeeder = new AnimalFeederGeneric<Cat>(Cat.class)
            List<Cat> fedAnimals = catFeeder.feed(animals);

            assertTrue(fedAnimals.size() == 1);
            assertTure(fedAnimals.get(0) instanceof Cat);
