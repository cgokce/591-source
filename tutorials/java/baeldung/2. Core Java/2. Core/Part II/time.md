#### Java 8 Time Overview

- Java 8 introduces two new classes for dates
    - Period: uses date-based values
    - Duration: uses time-based values
- Both classes can be used to represent an amount of time or determine the difference between two dates

Period Class
- Uses the units year, month and day to represent a period of time.

        LocalDate startDate = LocalDate.of(2015, 2, 20);
        LocalDate endDate = LocalDate.of(2017, 1, 15);

        Period period = Period.between(startDate, endDate);

        // Get period in terms of date units: years, months, days
        period.getYears();

        // Determine if the startDate < endDate
        assertFalse(period.isNegative())

        // Generate a period object is based on the number of days, months, weeks or years..
        Period fromDays = Period.ofDays(50);
        fromDays.plusDays(50).minusMonths(1).getMonths()

Duration Class
- Represents an interval of time in seconds or nanoseconds
- Most suited for handling shorter amount of time

        Instant start, end;
        ...
        Duration duration = Duration.between(start, end);

        // get seconds or nanoseconds
        duration.getSeconds()

        // Init with days, hours, milis, minutes
        Duration fromNanos = Duration.ofNanos(100);

        duration.plus(60, ChronoUnit.SECONDS).minus(30, ChronoUnit.SECONDS).getNanoseconds()