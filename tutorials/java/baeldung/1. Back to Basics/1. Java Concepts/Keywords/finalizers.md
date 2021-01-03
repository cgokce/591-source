#### Finalizers in Java

    baeldung.com/java-finalize

- finalize method is provided by the root Object class
    - A core aspect of the Java language
- This is called before the garbage collection for a particular object
- **Avoid using finalizers**, custom made finalizers can cause lots of problems
    - Use AutoClosable interface with overriding close method if needed
    - Deprecated with Java9

Using Finalizers
- Finalizer is the finalize() method
- Gets invoked when JVM figures out that this particular instance should be garbage collected
    - Such finalizer may perform any operations, including bringing the object back to life
- Main purpose of finalizer: **to release resources used by objects before they're removed from the memory**
- Primary mechanism for clean-up operations, or as a safety-net when other methods fail

        // Finalizable class uses a reader, and didnt close it
        public class Finalizable {
            private BufferedReader reader;

            public Finalizable(){
                ...
            }

            public readFirstLine() throws IOException {
                String firstLine = reader.readline();
                return firstLine
            }


            // Declare it just like any normal instance method

            @Override
            public void finalize() {

                try  {
                    reader.close();
                    System.out.println("Closed BufferedReader in the finalizer");
                } catch (IOException e) {
                    // ...
                }
            }


        }
- The time at which the garbage collector calls finalizers is dependent on the JVM's implementation and the system's conditions
    - Which are out of our control
- To make garbage collection happening on the spot, we'll use System.gc method, but we shouldnt use it in real applications
    - Its costly, doesnt trigger gc immediately, JVM knows better when GC needs to be called
    - If we need to force GC, we can use jconsole for that


---

Avoiding Finalizers
- There are many disadvantages
- Lack of promptness, we cannot know when a finalizer runs since garbage collection may occur anytime
- System resources aren't unlimited, **we might run out of resources before a clean-up happens, might result in a system crash**
- Disadvantage on program's portability. JVM is very portable, yet our finalizer might have worse performance
- Performance cost; JVM must perform many more operations when constructing and destroying object with finalizer
- Lack of exception handling during finalization: 
    - If a finalizer throws an exception, finalization process stops, leaving object in a corrupted state without any notification
- Eg, build a finalizer and generate object at each for loop

        public class CrashedFinalizable {

            @Override
            protected void finalize() {
                System.out.print("");
            }

            public static void main(String[] args) throws RefloectiveOperationException {
                for (int i=0; ;i++){
                    new CrashedFinalizable();
                }
            }
        
        }

        // Generates error during the loop execution
        // Exception in thread "main" java.lang.OutOfMemoryError: GC overhead limit exceeded
        // If we remove finalizer, program can run forever
- Explanation
    - Understand why the garbage collector didn't discard objects as it should we need to look at how the JVM works internally
    - When generating object (referent with finalizer), JVM generates an accompanying reference object of type java.lang.ref.Finalizer
        - After the referent is ready for garbage collection, the JVM marks the reference object as ready for processing and puts it into a reference queue
        - We can access this queue via the static field queue in the java.lang.ref.Finalizer class
    - Special daemon thread called Finalizer keeps running and looks for objects in the reference queue
        - When it finds one, it removes the reference object from the queue and calls the finalizer on the referent
    - During the next garbage collection cycle, the referent will be discarded - when it's no longer referenced from a reference object
    - If a thread keeps producing objects at a high speed, which is what happened in our example
        - Finalizer thread cannot keep up, eventually memory won't be able to store all the objects
    - In short: **Finalizers are very expensive**


Example without finalizer
- The class implements AutoClosable interface
- We also call the function at try with resources block


        public class CloseableResource implements AutoCloseable {
            private BufferedReader reader;

            // methods to use reader

            @Override
            public void close() {
                try {
                    reader.close();
                    System.out.println("Closed BufferedReader in the close method");
                } catch (IOException e) {
                    // handle exception
                }
            }
        }

        // Calling test method
        // Leaves the resources after finishing its job

        @Test
        public void testAndCloseResources() throws IOException {

            try (CloseableResource resource = new CloseableResource) {
                String firstLine = resource.readFirstLine();
            }

        }
