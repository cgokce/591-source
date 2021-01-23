#### Anonymous Classes in Java

Anonymous Class Declaration
- Inner classes with no name
- Since they have no name we can't use them in order to generate instances of anonymous classes
- We have to declare and instantiate anonymous classes in single expression at the point of use
- We may either extend an existing class or implement an interface

Extend a Class
- When we instantiate an anonymous class from an existent one

        # new name_of_class(constructor_arguments){method declarations}
        new ParentClass(...){...}

        # Parent constructor needs a string book name 
        new Book("Design Patterns"){
            @Override
            public String description(){
                return "Famous GoF book.";
            }
        }

Implement an Interface
- We may instantiate an anoymouıs class from an interface

        # new name_of_inteface(){method implementations}
        new InterfaceName(){...}

        # Since Java interfaces have no constructors, parantheses will always be empty
        new Runnable(){
            @Override
            public void run(){
                ...
            }
        }

Assigning to a variable
- Once we have instantiated anonymous class, we can assign that instance to a variable to reference it layer
- It is achieved via standard syntax

        Runnable action = new Runnable(){
            @Override
            public void run(){
                ...
            }
        };

        // We can also add it directly to a list
        List<Runnable> actions = new ArrayList<Runnable>();

        actions.add(new Runnable(){
            @Override
            public void run(){
                ...
            }
        });


Constructor
- Can not implement multiple interfaces
- During construction, there might exist exactly one instance of anonymous class, they cannot be abstract
- Since they have no name, we can not extend them
- For the same reason, anonymous classes cannot have explicitly declared constructors
- Lack of constructor is not a problem because
    - We generate anonymous instances as the same moment we declare them
    - From the instance, we can access local variables and enclosing class members

Static Members
- Anonymous Classes cannot have any static members except for those that are constant
- It will generate compiler error

Scope of Variables
- Anonymous classes capture local variables that are in the scope of the block in which we have declared the class
- In order to use local variables they must be effectively final (no need to decide with keyword but must not change)
- So, an anonymous class can access all members of its enclosing class

        int count = 1;
        Runnable action = new Runnable(){
            @Override
            public void run(){
                System.out.println("Runnable with captured variables" + count);
            }
        }


Use Cases
- Class Hierarchy and Encapsulation 
    - Achieves cleaner hierarchy of classes. It allows us to achieve finer encapsulation of class's data
- Cleaner Project Structure
    - Useful when we have to modify on the fly the implementation of methods of some classes
    - We can avoid adding new *.java fiels to the project in order to define top-level classes
- UI Event Listerenrs
    - It is useful when implementing UI classes
    - Still recommended way is usage of the lambdas since Java 8

            button.addActionListener(new ActionListener(){
                public void actionPerformed(ActionEvent e){
                    ...
                }
            });

General Picture
- It is an instance of a nested class
