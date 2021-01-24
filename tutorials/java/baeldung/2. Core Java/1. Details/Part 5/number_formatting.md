#### Number Formatting in Java

    https://www.baeldung.com/java-number-formatting

Basic formatting with String#format
- Method is very useful for formatting numbers
- Method takes two arguments: how many decimals we want to see, given value

        double value = 4.235298d;

        assertThat(String.format("%.2f", value)).isEqualTo("4.24");

Decimal Formatting by rounding
- Two primitive types representing decimals

        double myDouble = 7.8723d;
        float myFloat = 7.8723f;

- Using Big Decimal for formatting
    - By setting scale we provide number of decimal paces we want and how we want to round our number

            double D = 4.2345298d;
            assertThat(withBigDecimal(D, 2)).isEqualTo(4.24);

- Using Math.round()
    - Adjust the number of decimal places by multiplying and later dividing by 10^n, not very useful

Formatting Different Types
- Large integers with Commas

        DecimalFromat df = new DecimalFormat("###,###,###");
        return df.format(value)
        // 123,456,789
    
- Padding a Number

        String.format("%03d", 1)  // Output: 001

- Formatting Numbers with two zeros after decimal

        DecimalFormat df = new DecimalFormat("#.00");
        Double(df.format(value));

- Formatting and Percantages

        NumberFormat nf = NumberFormat.getPercentInstance(new Locale("en", "US));
        nf.format(25f / 100f); // 25%

- Currency Number Formatting

        NumberFormat nf = NumberFormat.getCurrencyInstance(new Locale("en", "US"))
        nf.format(23_500) // Output: 23,500.000


Advanced Formatting Use Cases
- DecimalFormat is one of the most popular ways to format a decimal in Java

        DecimalFormat df = (DecimalFormat) NumberFormat.getNumberInstance(Locale.getDefault());
        Double d = df.format(4.235298d)  //Output: 4.235 