#### Case-Insensitive String Matching

    https://www.baeldung.com/java-case-insensitive-string-matching

- There are multiple ways to check if String have substring
    - String.contains() have case insensitive workarounds

Solutions
- String.toLowerCase()
    - Simplest solution, we'll transform both strings to lowercase

            assertTrue(src.toLowerCase().contains(dest.toLowerCase()));

- String.matches() with regular expressions
    - (?i) enables case-insensitivity

        assertTrue(src.matches("(?i).*" + dest + ".*"));

- String.regionMatches()
    - Checks if two String regions match, with ignoreCase = True parameter

        for (int i = src.length() - dest.length(); i >= 0; i--){
            if (src.regionMatches(true, i, dest, 0, dest.length())){...}
        }

- Pattern with the CASE_INSENSITIVE Option
    - java.util.regex.Pattern class provides us a way of matching strings using the matcher() method

            assertTrue(Pattern.compile(Pattern.quote(dest), Pattern.CASE_INSENSITIVE)
                .matcher(stc)
                .find());

- Apache Commons StringUtils.containsIgnoreCase

        assertTrue(StringUtils.containsIgnoreCase(src,dest));

- Performance Comparion
     - java.util.regex.Pattern is the fastest
     - others are similar in speed
     - String regex match is 10x slower, dont try to parse string with primitive functions
     - There is a clear performance improvement with Java11