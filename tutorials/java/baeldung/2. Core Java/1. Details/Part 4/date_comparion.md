#### Comparing Dates in Java

    https://www.baeldung.com/java-comparing-dates

- Focus on comparing dates using the Java 8 Date/Time API

Comparing Dates
- Generate sample LocalDate instances
- Compare two LocalDate objects by utilizing the isAfter(), isBefore() and isEqual() methods

        LocalDate firstDate = LocalDate.of(2019, 8, 10);
        LocalDate secondDate = LocalDate.of(2019, 7, 1);

        // isAfter() check if instance is after other specified date
        assertThat(firstDate.isAFter(secondDate), is(true));

        // isBefore() checks if the date instance is before the other date
        assertThat(secondDate.isBefore(firstDate), is(true));

        // isEqual() checks if a date represents the same point on the local timeline
        assertThat(firstDate.isEqual(firstDate), is(true))

        // Using Comparable interface
        assertThat(firstDate.equals(secondDate), is(false));

Comparing Date Instances Containing the Time Component
- How to compare two LocalDateTime instances, including both the date and the time

        ZonedDateTime firstTime = ZonedDateTime.of(...);
        ZonedDateTime secondTime = ZonedDateTime.of(...);

        assertThat(firstTime.isAfter(secondTime), is(true));
        assertThat(secondTime.isAfter(firstTİme), is(true));
        assertThat(firstTime.isEqual(firstTİme), is(true));

Additional Comparisons
- Comparing LocalDate and the LocalDateTime instances

        LocalDateTime timestamp = ...
        LocalDate localDateToCompare = ...

        assertThat(timestamp.toLocalDate().isEqual(localDateToCompare), is(true));
        
        LocalDateTime timestamp2 = ...
        // Truncates to the given level, eg. day or hour
        assertThat(timestamp.truncatedTo(DAYS).isEqual(timestamp2.truncatedTo(DAYS)));

        // Zoned Date Time can be also compared with truncating
        zonedTimestamp.truncatedTo(HOURS).isEquals(zonedTimestamp2.truncatedTo(HOURS));

Comparison in the Old Java Date API
- Before J8, we had to use java.util.Date and java.util.Calendar
    - They also have after(), before(), compareTo() and equals() method
- Design of previous date API had flaws: being complex and not thread safe
- Use the Joda Time library when working before J8
