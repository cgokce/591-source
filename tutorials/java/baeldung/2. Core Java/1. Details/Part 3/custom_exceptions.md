#### Custom Exceptions on Java

    https://www.baeldung.com/java-new-custom-exception

Need for Custom Exceptions
- Main reasons for introducing custom exceptions are:
    - Business logic exceptions - Exceptions that are specific to the business logic and workflow
    - Catch and provide specific treatment to a subset of existing Java exceptions
- Java exceptions can be checked and unchecked

Custom Checked Exception
- Need to be treated explicitly
- Extend java.lang.Exception class
- We also add throwable as param to does not track the root cause when wrapping

        public class IncorrectFileNameException extends Exception {
            public IncorrectFileNameException(String errorMessage, Throwable err) {
                super(errorMessage);
            }
        }

        // eg usage with wrapping around another exception

        try {...
        } catch {
            if (!isCOrrectFileName(fileName)){
                throw new IncorrectFileNameException("Incorrect filename: " + fileName, err);
            }
        }

Custom Unchecked Exception
- Extend the java.lang.RuntimeException class
- This error will only be detected during runtime

        public class IncorrectFileExtensionException extends RuntimeException {
            public IncorrectFileExtensionException(String errorMessage, Throwable err){
                super(errorMessage, err);
            }
        }

        // usage
        try{...
        }catch(IllegalArgumentException err){
            if(!containsExtension(fileName)) {
                throw new IncorrectFileExtensionException("Filename does not contain extension :" + filename, err);
            }
        }