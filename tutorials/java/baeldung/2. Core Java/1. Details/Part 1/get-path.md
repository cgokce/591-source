#### Get Path Methods Comparison

    https://www.baeldung.com/java-path

java.io class has three get file methods to obtain the filesystem path

- Folder Structure used in examples
        |-- baeldung
            |-- foo
            |   |-- foo-one.txt
                \-- foo2
                    \-- foo3
                    |   \-- foo-two.txt
            

Methods
- getPath()
    - Returns String representation of the file's abstract pathname
     - Exact pathname passed to the File constructur
    - If the File object was generated using a relative path returned path will be relative
        - Returned string always uses the platform's default name-seperator character

                File file = new File("foo/foo-one.txt");
                String path = file.getPath();
                // on unix systems: foo/foo-one.txt
                // on windows sys:  foo\foo.txt

- getAbsolutePath()
    - Pathname of the file after resolving the path for the current user directory
    - Shorthand representations are not resolved further
        
            file.getAbsolutePath();

            // on unix: /home/username/baeldung/foo/foo2/../foo-two.txt
            // on windows: C:\Users\username\baeldung\foo\foo2\..\foo-one.txt
    
    

- getCanonicalPath()
    - Resolves the absolute pathname as well as the shorthands or redundant names like "." and ".."
    - It also resolves symbolic links on Unix systems and converts the drive letter to standard case on Windows

            // on unix: /home/username/baeldung/foo/foo2/foo3/foo-two.txt
            // on windows: C:\Users\username\baeldung\foo\foo2\foo3\foo-two.txt
    
    - Eg. use when data need fully qualified name, to be written into a database
        - It comes with a performance cost, if we know there are no redundant name we can also use absolutePath



