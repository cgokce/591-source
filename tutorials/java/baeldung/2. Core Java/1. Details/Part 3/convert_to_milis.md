#### Convert Time to Miliseconds

    https://www.baeldung.com/java-time-milliseconds

- Multiple ways of converting time into Unix-epoch miliseconds in Java

Core Java
- Using date

        Date date = ...

        // Returns miliseconds
        long millis = date.getTime()

- Using Calendar

        Calendar calendar = ...
        long millis = calendar.getTimeinMillis


Java 8 Date Time API
- Using Instant
    - Instant is a point in Java's epoch timeline

            java.time.Instant instant = ...
            long millis = instant.toEpochMilli();

- Using LocalDateTime
    
        LocalDateTime localDateTime = ...
        ZonedDateTime zdt = ZonedDateTime.of(localDateTime, ZoneId.systemDefault());
        long millis = zdt.toInstant().toEpochMilli();


Before Java 8
- We can use joda-time features, it is widely used library before java8