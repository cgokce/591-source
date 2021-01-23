#### Converting a Stack Trace to a String

- When dealing with exceptions in Java, we're ferquently logging or simply displaying stack traces
- Sometimes we don't want just to print the stack trace
    - We might need to write the stack trace to a files
    - To a database or event ransmit it over the network
- For above reasons, having the stack trace as a String would be very useful
    
Conversion with Core Java
- Function printStackTrace() of Exception class can take either a PrintStream or a PrintWriter

        StringWriter sw = new StringWriter();
        PrintWriter pw = new PrintWriter(sw);
        e.printStackTrace(pw);
        
        String stringStackTrace = sw.toString();

Conversion with Commons Lang
- Apache Commons Lang makes it very simple

        String stacktrace = ExceptionUtils.getStackTrace(e);