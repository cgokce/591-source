#### Java Copy Constructor

    https://www.baeldung.com/java-copy-constructor

- Copy constructor is a constructor that generates an object using another object of the same Java class
- Useful when copying object with multiple fields, or when we want to make a deep copy of existing object

Copy Constructor
- We declare a constructor that takes object of the same type as param
- Example of shallow copy, since all types are either primitive or immutable

        public class Employee {

            private int id;
            private String name;

            public Employee(Employee employee){
                this.id = employee.id;
                this.name = employee.name;
            }
        }

Copy Constructor vs Clone
- We can also use clone method to generate an object form an existing object
- Choose to avoid clone() for following reasons:
    - Copy constructor is much easier to implement, we dont need a Cloneable interface and handle CloneNotSupportedException
    - The clone method returns a general Object reference, we also need to typecast it
    - We can not assign a value to a final field in the clone method. However, we can do so in the copy constructor.

Inheritance Issues
- Copy constructors in Java are not inheritable by subclasses
- If we try to intialize a child object from a parent class reference we will face a casting issue

        public class Manager extends Employee {
            private List<Employee> directReports;

            public Manager(Manager manager) {
                super(manager.id, manager.name, manager.startDate);
                this.directReports = directReports.stream()
                    .collect(Collectors.toList());
            }
        }

        // Declare employee variable and instantiate it with the manager constructor
        Employee source = new Manager(1, "Baeldung Manager", startDate, directReports);

        // Since reference type is Employee, we have to cast it to Manager so we can use copy const
        // ERROR: ClassCastException
        Employee clone = new Manager((Manager) source);

        // SOLUTION: Generate a new inheritable method for both classes eg. copy() method
        Employee clone = source.copy();