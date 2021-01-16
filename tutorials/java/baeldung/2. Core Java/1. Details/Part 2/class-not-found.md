#### When JVM Can not find the class

    https://www.baeldung.com/java-classnotfoundexception-and-noclassdeffounderror

- When JVM can not find a requested class on the classpath, two exceptions occur
    - ClassNotFoundException -> Trying to load a class at runtime only
    - NoClassDefFoundError -> Class was present at compile time, but runtime could not find in classpath
- There are some core differences between these two

ClassNotFound Exception
- Checked exception
- Occurs when an application tries to load a class through its fully-qualified name
    - Can not find its definition on the classpath
- Mainly when ctrying to load classes using 
    - Class.forName()
    - ClassLoader.loadClass()
    - ClassLoader.findSystemClass()
- Need to careful working with reflection
- Eg. load JDBC driver without adding dependencies

        @Test(expected = ClassNotFoundException.class)
        public void givenNoDrivers_whenLoadDriverClass_thenClassNotFoundException() throws ClassNotFoundException {
            Class.forName("oracle.jdbc.driver.OracleDriver");
        }


NoClassDefFoundError
- Fatal error, occurs when JVM Cant find the definition of class while
    - Instantiate a class by using the new keyword
    - Load a class with a method call
- Occurs when 
    - Compiler could successfully compile the class
    - But Java runtime couldn't locate the class file
- Usually happens when there is an exception while executing a static block or initializing static fields of the class
- Eg. loading a class with init errors

        public class ClassWithInitErrors {
            static int data = 1/0;
        }

        public class NoclassDefFoundErrorExample {
            public ClassWithInitErrors getClassWithInitErrors() {
            ...
            }
        }

        @Test(expected = NoClassDefFoundError.class)
        public void givenInitErrorInClass_whenLoadClass_thenNoClassDefFoundError(){
            NoClassDefFoundErrorExampl sample = new NoClassDefFoundErrorExample();
            sample.getClassWithInitErrors();
        }

Resolution
- It can be time-consuming to diagnose and fix given errors
- Reason is that classPath is not available in the classpath at runtime
- Few approaches:
    - Make sure whether class or jar containing class is available in classpath
    - If available in app classpath, probably classpath is getting overridden. We need to find exact classpath
    - If application is using multiple class loaders, classes loaded with one classloaders might not be available to other
