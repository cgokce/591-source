#### RegEx for matching date patterns

    https://www.baeldung.com/java-date-regular-expressions

- We'll use java.util.regex package to determine whether a given String contains a valid date or not.

Example data format regex search
- Consider using LocalDate.parse() if validation for date needed
    - This is just an example tp show regex
- Define valid date: YYYY-MM-DD
- February 29 is only at leap date

Implementation
- Build pattern then apply matcher

            private static Pattern DATE_PATTERN = Pattern.compile (..regex..);
            String date = "..."

            String DATE_PATTERN.matcher(date).matches();
- Parsing complex regular expressions may significantly affect performance of execution flow
