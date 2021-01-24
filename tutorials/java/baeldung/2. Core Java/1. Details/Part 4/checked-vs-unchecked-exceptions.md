#### Checked and Unchecked Exceptions in Java

    https://www.baeldung.com/java-checked-unchecked-exceptions

Checked Exceptions
- Represents errors outside the control of the program
- Java verifies these at compile-time, throws keyword is used to declare a checked exception
- Eg. IOException, SQLException, ParseException

        private static void checkedExceptionWithThrows() throws FileNotFoundException {
            FileInputStream stream = new FileInputStream(...);
        }

        // We can catch the exception
        private static void checkedExceptionWithTryCatch(){
            try {
                FileInputStream stream = new FileInputStream(...);
            } catch(FileNotFoundException e){
                e.printStackTrace();
            }
        }

        // Generate new custom checked exception
        public class IncorrectFileNameException extends Exception(){
            public IncorrectFileNameException(String errorMessage){
                super(errorMessage);
            }
        }

Unchecked Exceptions
- Reflects some error inside the program logic, eg dividing number by 0 results in ArithmeticException
- Java does not verify unchecked exceptions at compile time, there is no need for throws keyword
- Eg. NullPointerException, ArrayIndexOutOfBoundsException, IllegalArgumentException

        // Generating a custom unchecked exception
        public class NullOrEmptyException extends RuntimeException {
            public NullOrEmptyException( String errorMessage){
                super(errorMessage);
            }
        }

When to use them
- Checked Exception: If a client can reasonably be expected to recover from an exception
- Unchecked Exception: If a client cannot do anything to recover from the exception

        // Checked Exception, user input file name is invalid
        if (!isCorrectFileName(fileName)){
            throw new IncrorrectFileNameException("Incorrect filename: " + fileName);
        }

        // Unchecked exception, input file name is null pointer or empty string, means we have errors in code
        if (fileName == null || fileName.isEmpty()){
            throw new NullOrEmptyException("The filename is null or empty.");
        }

