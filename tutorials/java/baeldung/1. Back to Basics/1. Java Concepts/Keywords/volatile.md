#### Volatile Keyword in Java

    https://www.baeldung.com/java-volatile

- In the absence of necessary synchronizations, the compiler runtime, or processors may apply all sorts of optimizations
    - Caching and reordering are among optimzations that may surprise us in concurrent context.
    - Java and the JVM provide many ways to control memory order, eg. volatile keyword

---

Shared multiprocessor architecture
- Processors are responsible for executing program instructions.
    - Need to retrieve both program instructions and required data from RAM
- CPUs are capable of carrying out a significant number of instructions per second
    - Fetching from RAM is not that ideal for them
- To solve this, processors use tricks like
    - Out of order execution
    - Branch Prediction
    - Speculative Execution
    - Caching
- As different cores execute more instructions and manipulate more data
    - They fill up their caches with more relevant data and instructions
    - Improve overall performance at the expense of introducing cache coherence challenges
- SIMPLY: We should think twice about what happens when one thread updates a cached value

![Shared Multi-Processor Architecture](https://www.baeldung.com/wp-content/uploads/2017/08/cpu.png)

---

Failure Case of a Thread
- Sample TaskRunner generates another thread and waits until main thread signals ready.

        public class TaskRunner {

            private static int number;
            private static boolean ready;

            private static class Reader extends Thread {

                @Override
                public void run() {
                    while (!ready) {
                        Thread.yield();
                    }

                    System.out.println(number);
                }
            }

            public static void main(String[] args) {
                new Reader().start();
                number = 42;
                ready = true;
            }
        }

- This program is expected to print 42 after a short delay
    - FAIL: Delay can be much longer
    - FAIL: It can event print zero!
- Cause of these anomalities is the lack of proper memory visibility and reordering


#### Cause of Failures

1. Memory Visibility
- In example we have two application threads.
    - Main thread and the reader thread.
    - Imagine a scenario which the OS schedules those threads on two different CPU cores:
        - Main thread has its copy of ready and number variables in its core cache
        - Reader tread ends up with its copies too
        - Main thread updates the cached values
- On most modern processors, write requests won't be applied right away after they're issued
    - In fact, processors tend to queue those writes in a special write buffer
    - After a while they will apply those writes to main memory all at once
- When the main thread updates the number and ready variables
    - No guarantee about reader thread
    - Reader thread may see right away, or with a delay, or never at all
- May cause liveness issues in programs that are relying on visibility

2. Reordering
- Reader may see those writes in any order other than the actual program order
- We may see 0 as the printed value!
- Reordering is an optimization technique for performance
    - Processor may flush its write buffer in any order other than the program order
    - Processor may apply out-of-order execution technique
    - The JUT compiler may optimize via reordering

---

#### Volatile Application

1. *volatile* Keeps the Memory Order
- To ensure updates to variables propagate predictabley to other threads, we should apply the volatile modifier

        public class TaskRunner {

            private volatile static int number;
            private volatile static boolean ready;

            // same as before
        }
- This way we communicate runtime and processor to not reorder any instruction involving volatile variable.
    - Processors should flush any updates to these variables right away

2. *volatile* and Thread Syncronization
- For multithreaded applications, we need to ensure a couple of rules for consistent behavior
    - Mutual Exclusion -> Only one thread executes a critical section at a time
    - Visibility -> Changes made by one thread to the shared data are visible to other threads to maintain consistency
- Syncronized methods and blocks provide both of above properties at cost of application performance
- Volatile can help **ensure visibility aspect** without mutual exclusion
- Volatile is useful when
    - Where we're ok with multiple threads executing a block of code in parallel
    - But we need to ensure the visibility property

3. Happens-Before Ordering
- Memory visibility aspect of volatile variables extend beyond the volatiles themselves
- Eg. Thread A writes to a volatile variable and then thread B reads the same volatile variable
    - The values that were visible to A before writing the volatile variable
    - Visible to B after reading the volatile variable
- Any write to a volatile field happens before every subsequent read of same field
    - Volatile variable rule of the Java Memory Model

![Volatile Visibility Ordering](https://www.baeldung.com/wp-content/uploads/2017/08/happens-before.png)

4. Piggybacking
- Using happens-before ordering
    - We can piggyback on the visibility properties of another volatile variable
- Anything prior to writing true to the ready variable is visible to anything after reading ready
- Number variable piggybacks on memory visibility is enforced by read variable
    - Other variables also forcible exhibiting a volatile behavior
- We can define only few variables in our class as volatile and optimize the visibility guarantee