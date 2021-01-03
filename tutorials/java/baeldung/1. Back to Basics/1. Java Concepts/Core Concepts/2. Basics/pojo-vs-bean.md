#### POJO Class - Plain Old Java Object

    https://www.baeldung.com/java-pojo-class

Plain Old Java Objects
- Describing a straightforward type with no references not tied to any particular framework
- POJO is just a naming convention for our properties and methods

        // Eg. Simple pojo without any convention
        public class EmployeePojo {
            public String firstName;
            public String lastName;
            private LocalDate startDate;
            ...
            public String name(){...}
            public LocalDate getStart(){...}
        }
- There is no convention for constructing, accessing or modifying class's state
- Lack of convention can cause problems:
    - Increases the learning curve for coders trying to understand or use it
    - May limit a framework's ability to favor convention over configuration


Limitations
- Reflection with a POJO
    - To inspect Add commons-beanutils-dependency to project, PropertyUtils functions
        - Only finds *start* as a property of the class
        - PropertyUtils failed to find the other two
    - Libraries such as *Jackson* will have problems processing the EmployeePojo
    - Ideally we want to see all of our properties: firstName, lastName and startDate.
        - JavaBean naming convention is solution, many libraries support it

JavaBean
- It is still a POJO but introduces a strict set of rules around how we implement it.
    - **Access Levels** -> Properties are private and we expose getters and setters
    - **Method Names** -> Getters and setters follow the getX and setX convention (Booleans can use isX convention)
    - **Default Constructor** -> No-argument constructor must be present
        - Eg. Instance can be generated without providing arguments, eg. deserialization
    - **Serializable** -> Implementing the Serializable interface allows us to store the state
- Convert previous example to EmployeeBean

        public class EmployeeBean implements Serializable {
            private static final long serialVersionUID = -52389238423;
            private String firstName;
            private String lastName;
            private LocalDate startDate;

            public EmployeeBean() {
            }

            public String getFirstName(){...}
            public void setFirstName(String firstName){...}
            ... 
            //Other getters and setters
            ...
        }
- Reflection with Java Bean
    - When we inspect bean reflection, now we get the full list of the properties
            
            [firstName, lastName, startDate]

---

Tradeoffs When Using JavaBeans
- Java Beans are helpful but every design choice comes with tradeoffs
- Frameworks also have been adapted to other bean conventions over the years
- Mutability
    - Mutable due to setter methods, could lead to concurrency or consistency issues
- Boilerplate
    - We must introduce getters for all properties and setters for most, mighe be unnecessary
- Zero-Argument Constructer
    - We often need arguments in our constructors to ensure the object gets instantiated in a valid state
    - But JavaBean standard requires us to provide zero arg vonstructors
