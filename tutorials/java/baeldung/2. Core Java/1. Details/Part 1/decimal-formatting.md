#### Decimal Formatting

    https://www.baeldung.com/java-round-decimal-number

Decimal Numbers
- Two primitive types can be used for storing decimals, float and double.
    - Double is default
- BigDecimal class should be used for precise values and rounding eg. for currencies

Decimal Formatting
- Print a decimal with n digits after decimal points
- Format Output with print

        double PI = 3.1415;
        System.out.println("Three precision after decimal point %.3f", PI);

- Format with DecimalFormat class
    - Allows us to explicitly set rounding behavior

        DecimalFormat df = new DecimalFormat("***.***");
        System.out.println(df.format(PI));

---

Rounding
- BigDecimal Rounding
    - To round double to n decimal places, we can write a helper method
        - When constructing BigDecimal, **always use BigDecimal(string) constructor.
        - Prevents issues with representing inexact values

            private static double round(double value, int places){

                BigDecimal bd = new BigDecimal (Double.toString(value));
                bd = bd.setScale(places, RoundingMode.HALF_UP);
                return bd.doubleValue();

            }
- Apache Commons Module Rounding
    - By default, using the same HALF_UP rounding as in previous example.
            
            Precision.round(PI, 3);

- Math.round() Method - not recommended!
    - We can control n number of decimal by multiplying and dividing by 10^n.
    - **Not recommended as it's truncating the value**
            double scale Math.pow(10, scales);
            double output = Math.round(value*scale) / scale;

    