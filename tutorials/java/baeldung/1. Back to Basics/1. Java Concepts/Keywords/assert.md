#### Java Assertions

    https://www.baeldung.com/java-assert

Assert Keyword
- Assert keyword allows developers to quickly verify certain assumptions or state of a program
- Introduced in 1.4, have been around for quite a long time
- Can drastically reduce boilerplate and make our code more readable
        
        // Previously
        if(conn == null) {
            throw new RuntimeException("Connection is null");
        }

        // With assert
        assert conn != null : "Connection is null";

        // It will automatically throw AssertionError
        Exception in thread "main" java.lang.AssertionError: Connection is null
        at com.baeldung.assertion.Assertion.setup(Assertion.java:15)
        at com.baeldung.assertion.Assertion.main(Assertion.java:10)

- Do not need to use *if and throw block*, assert is doing it more readable
- JVM disables assertion validation by default, -enableassertions or -ea command

Handling an Assertion Error
- AssertionError extends Error, which extends Throwable.
    - Meaning AssertionError is unchecked exception
    - There is no need for decleration and no need to try to catcj
    - AssertionErrors are meant to indicate **unrecoverable conditions** in an application
    - Never try to handle them or attempt recovery

Best Practices
- They can be disabled so never assume they'll executed
- Always check for null values and empty Optionals when appropriate
- Avoid using assertions to check inputs into a public method
    - Instead use an unchecked exception such as IllegalArgumentException or NullPointerException
- Don't call methods in assertion conditions
    - Instead assign the result of the method to a local variable
    - Use that variable with assert
- Assertions are great for places in code that never will be executed
    - Eg. default case of a switch statement
    - Eg. After a loop that never finishes