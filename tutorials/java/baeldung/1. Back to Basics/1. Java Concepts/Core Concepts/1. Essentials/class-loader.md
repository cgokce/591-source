#### Class Loaders

    https://www.baeldung.com/java-classloaders

- Responsible for loading Java classes during runtime dynamically to the JVM
    - They are part of the JRE
    - JVM doesn't need to know about the underlying files or file systems in order to run Java programs
- Normally classes aren't loaded into memory all at once, but when required by an application
    - Class Loaders -> Responsible for loading classes into memory

---

**Types of Built-in Class Loaders**

- Bootstrap
    - Bootstrap or primordial class loader is the parent of all the others
    - Custom java classes are loaded by an instance of java.lang.ClassLoader
    - ClassLoaders are classes themselves, who loads the java.lang.ClassLoader itself?
        - Bootstrap/Primordial loader responsible for loading JDK internal classes.
    - Typically rt.jar and other core libraries located in $JAVA_HOME/jre/lib directory
        - https://stackoverflow.com/questions/3091040/why-do-we-use-rt-jar-in-a-java-project
        - Bootstrap class loader serves as a parent of all the other ClassLoader instances

                ArrayList.class.getClassLoader());
                // Class loader of ArrayList:null
    - For ArrayList it displays null in the output
        - Because bootstrap class loader is written in the native code, not Java
        - Doesn't show as a Java Class
- Extension
    - Child of the bootstrap class loader and takes care of loading the extensions of the standard core Java classes
    - Loads classes that are extension of the standard core Java classes
    - Usually from $JAVA_HOME/lib/ext directory or any other directory mentioned in java.ext.dirs system property

                Logging.class.getClassLoader());
                // Class loader of Logging:sun.misc.Launcher$ExtClassLoader@3caeaf62
- Application/System Class Loader
    - Child of a Extensions class loader
    - Application or system class loader loads our own files in classpath
    - Loads files found in the classpath environment variable (-classpath command line option)

                myClass.class.getClassLoader());
                // Class loader of this class:sun.misc.Launcher$AppClassLoader@18b4aac2

---

How does it work
- When JVM requests a class
    - java.lang.ClassLoader.loadClass() method
    - Class loader tries to loacte the class and load the class definition into the runtime
    - Try to load using fully qualified class name
    - If class ins't already loaded, delegates the request to the parent class loader, do it recursively
- If the last child class loader is not able to load the class, throws NoClassDefFoundError or ClassNotFoundException

        java.lang.ClassNotFoundException: com.baeldung.classloader.SampleClassLoader    
        at java.net.URLClassLoader.findClass(URLClassLoader.java:381)    
        at java.lang.ClassLoader.loadClass(ClassLoader.java:424)    
        at java.lang.ClassLoader.loadClass(ClassLoader.java:357)    
        at java.lang.Class.forName0(Native Method)    
        at java.lang.Class.forName(Class.java:348)
- Delegation model is used
    - On request to find a class or resource, a ClassLoader instance will delegate the search of the class resource to parent
        - system -> extension -> bootstrap  -----> Then look in reverse order
    - It is **easy to ensure unique classes** as we always try to delegate upwards
    - Children class loaders are **visible** to classes loaded by its parent class loaders

---

Custom Class Loader
- Used in scenarios where we need to load classes out of the local drive or a network
- Use cases
    - Helping in modifying existing bytecode, eg. weaving agents (AspectJ, Cross cutting concerns, AOP)
    - Generating classes dynamically suited to user's needs
        - eg in JDBC switching between different driver implementations is through dynamic class loading
    - Implementing a class versioning mechanism
        - Loading different bytecodes for classes with same names and packages
- Eg. browsers use a custom class loader to load executable content from a website
    - Applets from different web pages using seperate class loaders
    - Load raw bytecode via HTTP and turn them into classes inside the JVM
    - Even applets have same name, they are considered different components if loaded by different class loaders

Context Classloader
- Does not follow a hierarchical model for delegation
- Eg use case independent vendor class loading at runtime, need visibility in reverse
- Java lang thread class returns ContextClassLoader for the particular thread, provided by the generator of thread