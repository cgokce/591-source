#### Syncronized Block Usage

- In a multi-threaded environment, a race condition occurs when two or more threads attempt to update mutable shared data at the same time.
    - Java offers mechanism to avoid race conditions by synchronizing thread access to shared data
- Sycronized blocks **allowing only one thread to execute at any given time**

- Eg. synchronization error
    - Run the following with multiple threads 1000 times, result != 1000

        private int sum = 0;

        public void calculate() {
            setSum(getSum() + 1);
        }

--- 

Syncronized keyword can be used on different levels
- 1. Instance methods
    - Add the synchronized keyword in the method declaration to make the method syncronized
    - Only one thread per instance of the class can execute this method

            public synchronized void synchronisedCalculate() {
                setSum(getSum() + 1);
            }

- 2. Static methods
    - Static methods are synchronized just like instance methods
    - Synchronized on the Class object associated with the class 
    - Since only one object exists per JVM per class, only one thread can execute inside a static synchronized method per class  

             public static synchronized void syncStaticCalculate() {
               staticSum = staticSum + 1;
            }

- 3. Code blocks Within Methods
    - When we want to synchronize only some instructions inside a method
    
        public void performSynchronisedTask() {
            ...
            synchronized (this) {
                setCount(getCount()+1);
            }
            ...
        }

    - Passing this to synchronized method, this is the monitor object
    - Only one thread per monitor object can execute inside that block of code
    - If the method is static, we would pass the class name in place of object reference


----

**Reentrancy**
- Lock behind the synchronized methods and block is reentrant.
    - Current thread can acquire the same synchronized lock over and over again while holding it

        synchronized (lock) {
            System.out.println("Entering again");

            synchronized (lock) {
                System.out.println("And again");
            }
        }

