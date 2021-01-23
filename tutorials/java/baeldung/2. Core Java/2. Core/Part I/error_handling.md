#### Exception Handling in Java

    https://www.baeldung.com/java-exceptions

- Java code can experience errors while executing instructions
    - Good exception handling can handle errors and gracefully re-route program to give the user still a positive experience
- Ideal environment problem: Not always filesystem works, network health and JVM has memory
    - We must handle these conditions because they might terminate program
    - Stack trace is used to pinpoint error location without having to debug

Exception Hierarch
- Java objects extended from Throwable
- Three main categories
    - Checked exceptions: Java compiler requires us to handle
        - Either decleratively throw up to call stack or handle, eg. IO Exception
    - Runtime/Unchecked exceptions
        - eg. NullPointerException, IllegalArgumentException
    - Errors
        - Serious and usually irrecoverable, eg. library incompatability, infinite recursion or memory leaks
        - eg. StackOverflowError, OutOfMemoryError


                Throwable (checked)
                |               |
            Exception         Error
            (checked)      (unchecked)
                |
            Runtime Exception
            (unchecked)

    
Handling Exceptions
- In the Java API, plenty of places where things can go wrong and some of places are marked with exceptions
    - We must handle checked exceptions

            public Scanner(String filename) throws FileNotFoundException {...}

- throws
    - Simplest way to handle exception is rethrow it
    - Now any call on method needs to handle throed exception

            public int getPlayerScore(String playerFile) throws FileNotFoundException{
                Scanner contents = new Scanner(new File(playerFile));
            }

- try/catch
    - We can handle it by rethrowing in catch or recover it here

            try{
                Scanner contents = new Scanner(new File(playerFile));
                ...
            } catch (FileNotFoundException noFile){
                // option1: throw
                throw new IllegalArgumentException("File not found");

                // option2 : handle
                logger.warn("File not found resetting score");
                return 0;
            }
- finally
    - We have code that needs to execute regardless of whether an exception occurs
    - Even if exception is throuwn up the call stack, java will call the contents of finally before doing that
    - Try/catch/finally can be used together
    - Also finally block can have nested try statement

            try {
                ...
            } finally {
                if (contents != null){
                    contents.close();
                }
            }

- try-with-resources
    - More precise syntax when we want to close stream etc in finally, which needs to extend AutoCloseable

- Multiple catch Blocks
    - When code can throw more than one excveption we can have more than one catch block
    - When handling subclass exceptions, handle at top (eg. FileNotFound is subclass of IO)

            try{
                ...
            } catch (FileNotFoundException e) {
                ...
            } catch (IOException e){
                ...
            } catch (NumberFormatException e) {
                ...
            }

- Union catch Blocks
    - When we know the way we handle errors is same, we can handle multiple exceptions in same block

            try{
                ...
            } catch (IOException | NumberFormatException e){
                ...
            }

---

Throwing Exceptions
- If we don't want to handle exception ourselves
- We design an exception to use in examples

        public class TimeoutException extends Exception{
            public TimeoutException(String message){
                super(message);
            }
        }

- Throwing Checked Exception
    - We should throw when we are trying to indicate that something has gone wrong

            throw new TimeoutException("This operation took too long");

- Throwing Unchecked Exception
    - Eg if we want to validate input we can use an unchecked exception instead

            if(!isFilenameValid(playersFile)){
                throw new IllegalArgumentException("Filename isn't valid!");
            }

- Wrapping and Rethrowing
    - Can be beneficial wrapping multiple exception into one

        try {
            ...
        } catch (IOException | OtherException e) {
            throw new PlayerLoadException(e);
        }

- Rethrowing Thwrowable or Exception
    - If the only possible exceptions that a given block of code could raise are unchecked exceptions
    - Then we can catch and rethrow Throwable or Exception without adding them to our method signature
    - This is handy for proxy classes and methods

            try{
                throw new NullPointerException();
            }catch (Throwable t){
                throw t;
            }

- Inheritance
    - When we mark methods with a throws keyword, it impacts how subclasses can override our method
    - Subclasses can throw fewer checked exceptions than their superclass but not more

            public List<Player> loadAllPlayers(String playersFile) throws TimeoutException{...}
            
            @Override  //Less risky signature is ok
            public List<Player> loadAllPlayers(String playersFile){...}

            @Override //ERROR; BAD; TOO RISKY
            public List<Player> loadApllPlayers() thros MyCheckedException


Anti-Patterns
- Swallowing exception
    - It doesn't address the issue and keeps other code from being address it too
    - If we are sure that won't happen, we should at least add a comment and print out exception

            try{
                ...
            }catch(IOException e){
                //this will never happen
                // better way adding below kind of code
                logger.error("Coulnt load the score");
                return 0;
            }
- Using return in finally block
    - Bad because, by returning abruptly JVM will drop the exception
- Using throw in finally block
    - Will take predence over the current try catch, and erase it, and we will lose valuable information
- Using throw as a goto
    - Only use exceptions for error handling, not flow control