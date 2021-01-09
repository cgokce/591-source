#### StackOverflowError in Java

- One of the most common runtime errors in Java

Understanding Stack Frames
- Stack Frame: **Generated on the call stack when method is called**
    - Holds parameters of the invoked method: Local parameters, return address
- Stack frames will be generated until it reached end of method invocation
- StackOverflowError: When JVM encounters no available space during the process

StackOverflowError
- Most common cause is unterminated/infinite recursion
- Rare causes
    - Calling methods from within methods until stack is exhausted
    - Having a vast number of local variables inside a method
    - When application is designed to have cyclic relationship between classes
        - Constructors of each other is called repeatedly
    - Class is being instantiated within the same class as an instance variable of that class
        - Cause constructor of the same class to be called again and again recursively
- Eg. recursion without a base case

        public class UnintendedInfiniteRecursion {
            public int calculateFactorial(int number) {
                return number * calculateFactorial (number - 1);
            }
        }
- Eg. class constructors call each other 

        // constructor inside class
        public ClassOne() {
            ClassTwo instance = new ClassTwo();
        }

        public ClassTwo() {
            ClassOne instance = new ClassOne(); 
        }

        @Text(expected = StackOverflowError.class)
        public void whenInstanciatingClassOne_thenThrowsException() {
            ClassOne instance = new ClassOne();
        }
- Eg. Instantiate class within same class as instance variabl

        public class AccountHolder(){
            AccountHolder jointAccountHolder = new AccountHolder();
        }

        @Text(expected=StackOverflowError.class)
        public void whenInstanciatingAccountHolder_thenThrowsException(){
            AccountHolder sampleHolder = new AccountHolder();
        }

    


---

Dealing with StackOverflowError
- Inspect the stack trace to identify the repeating pattern of line numbers

        java.lang.StackOverflowError
        at c.b.s.ClassTwo.<init>(ClassTwo.java:9)
        at c.b.s.ClassOne.<init>(ClassOne.java:9)
        at c.b.s.ClassTwo.<init>(ClassTwo.java:9)
        at c.b.s.ClassOne.<init>(ClassOne.java:9)

- Fix the three sample causes that provides cause
- If still giving error, increase the stack size
- The **-Xss flag** can be used to increase the size of the stack.