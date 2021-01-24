#### Command-Line Arguments in Java

    https://www.baeldung.com/java-command-line-arguments

Accessing Command-Line Arguments
- Since the main() method is the entry point of a Java application
- JVM passes the command-line arguments through its arguments
- Traditional way is to use a String array

        public static void main(String[] main){...}

        // varargs ( similar to the array ): another way to call argument
        public static void main(String... args){...}

- Array contains the command-line arguments in the same order we passed at execution
- Array only contains the arguments (not the program name)

How to pass arguments
- Command line by after class name
    - Note everything passed before class name is considered as JVM argumnets

            java com.baeuldung.commandlinedemo hello world

            // Running the published jar file
            java -jar cli-example.jar hello world
    
- Using an IDE, eg. Eclipse, Intellij. It'll run with given arguments through GUI
- Third party libraries
    - Manual handling of command line arguments are mostly straightforwared
    - But with increasing complexity, we can use third-party library eg. Picocli or Spring Shell
