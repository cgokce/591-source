#### Java 9 Modules - Java Platform Modules System (JPMS)

    https://www.baeldung.com/java-9-modularity

Module
- **Group of closely related packages and resources along with a new module descriptor file**
- It is a package of Java Packages.
- Abstraction allows us to make our code event more reusable

Packages
- When we generate module, we organize code internally in packages
- Used to determine what code is publicly accessible outside of module

Resources
- **Each module is responsible for its resources, like media or configuration files**
- Previously we'd put all resources into root level of our project
- With modules we can ship required images and XML files with the module that needs it


Maven vs Java9 Module System

    https://itqna.net/questions/937/maven-module-vs-java-9-module

    Maven manages dependencies compile-time . Maven makes it easy to build software. Not just when compiling, but also when testing, packaging and distributing the software.

    Java Platform Module manages run-time dependencies . Only used at run time in the JVM (Java virtual machine).

---

Module Descriptor
- When we generate a module, we include descriptor file defines several aspacets of our new module
    - Name - name of the module
    - Dependencies - list of other modules that this module depends on
    - Public Packages - List of all packages we want accessible from outside module
    - Services Offered, Services Consumed, Reflection Permissions...
- By default packages are private
    - We need to list all packages we want to be public

Module Types
- System Modules: Including Java SE and JDK modules
- Application Modules: What we want to build when we decide to use modules.
- Automatic Modules: Adding existing JAR files to the module path
- Unnamed Module: Class or JAR is loaded onto the classpath, but not module path.

Distribution
- JAR file or "exploded" compiled project
- Only one module per java file is allowed

---

Module Declarations
- Put special file at root named: module-info.java
    - Known as the module descriptor and contains all of the data needed to build and use our new module

        module myModuleName {
            // optional directives
        }
- Directives 
    - Declare dependencies -> requires module.name;
    - Compile time-only dependencies -> requires static module.name;
    - Transitive dependencies -> requires transitive module.name;
    - Expose all public members of named package -> exports com.my.package.name
    - Expose to only some directive -> export com.my.package.name to com.specific.package
    - Give specific interface or abstract class as service -> uses class.name
    - Service provider that other modules can consume -> provides MyInterface with MyInterfaceImpl;
    - Allowing reflection of private types, dont want to expose all code -> opens com.my.package;
    - Encapsulation, allowing reflection to only some modules -> opens com.my.package to moduleOne, moduleTwo etc.;
- Commmand Line Options -> various options to manage and monitor
- Visibility
    - Lots of libraries depend on reflection eg. JUnit and Spring
    - By default in Java 9, we have only access to public classes methods and fields in our exported packages
    - We can use open, opens... to grant runtime-only access for relection

---

- Is there any need to switch to modules when migrating to Java 9+/Java 11?
        https://stackoverflow.com/questions/62950667/is-there-any-need-to-switch-to-modules-when-migrating-to-java-9-java-11

        There is no need to switch to modules.
        There has never been a need to switch to modules.
        ...
        If you maintain a large legacy project that isn’t changing very much, then it’s probably not worth the effort.

        If you work on a large project that’s grown difficult to maintain over the years then the clarity and discipline that modularization brings could be beneficial, but it could also be a lot of work, so think carefully before you begin.