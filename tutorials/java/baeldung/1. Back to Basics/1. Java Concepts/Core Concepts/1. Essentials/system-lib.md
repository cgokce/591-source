#### java.lang.System Class

IO 
- System.out
    - Points to the standard output stream, exposing it as a PrintStream
    - Print text to console

        System.out.print("some inline message")
    
        // Customize output location
        System.setOut(new PrintStream("filename.txt"))
- System.err
    - Also instance of a PrintStream
    - Represents standard error, used for output error messages
    - Consoles usually render error stream messages differently than output stream

        System.err.print("some inline error message");
- System.in
    - Points to the standard in, exposing as InputStream

        // Low level example, by default, InputStream is console
        byte[] name = new byte[length];
        System.in.read(name, 0, length);

        // More usable, it'll read after user pressing enter
        BufferedReader reader = new BufferedReader(
        new InputStreamReader(System.in));
        return reader.readLine();
    - We dont close the streams until end of the program, it can not be opened again

---

Utility Methods
- Accessing the console
    - Easier way accessing to console with Java6
    - Simply using System.out and in directly

            Console console = System.console();	 	 

            // Good practice to check for null when operating on console read       
            return console == null ? null :	 
            console.readLine("%s", "Enter your name: ");	
- Copying Arrays
    - System.arraycopy is old C-styleway of copying one into another

            System.arraycopy(a, 0, b, 0, a.length);
            assertArrayEquals(a,b);

            // starting a[1], starting at b[3], copy 2 elements
            System.arraycopy(a, 1, b, 3, 2);
    - Can throw:
        - NullPointerException: Any of array is null
        - IndexOutOfBoundsException: Copy references either array beyond its range
        - ArrayStoreException: Copy results in type mismatch
- Date and Time
    - Two methods related to time
    - currentTimeMillis -> number of miliseconds passed since Jan 1 1970

            new Date(System.currentTimeMillis()).toString();
    
    - nanoTime -> Returns the time relative to JVM startup
        - when called two times it is used to calculate passage of time in application

                long startTime = System.nanoTime();
                // ...
                long endTime = System.nanoTime();

                assertTrue(endTime - startTime < 10000);     
- Exiting the Program
    - System.exit(exit_code), exit code => 0: Success, others err
    - Exit code will get sent to the console or shell that launched the program
    - Better not to use in complex apps, it will take whole application down
- Accessing Runtime Properties
    - Properties specified via -D are accessible via getProperty.
    - -D is for seperating jvm params with user params (-X and -XX params are JVM advanced params)

            System.setProperty("some_prop", "some_val");
            assertEquals("some_prop", System.getProperty("some_val"));
- Accessing environment Variables
    - Read only access only
            System.getenv("PATH");
- Administering Garbage Collection
    - We might want to make a direct suggestion to the JVM
        - System.runFinalization -> Run Finalization Routine
        - System.gc -> Run Garbage Collection Routine
    - These methods does not guarantee the finalization or garbage collection
        - Usefullness are narrow, eg invoking gc when desktop app gets minimized