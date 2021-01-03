#### Introduction

    https://www.baeldung.com/java-binary-numbers

- Using binary numbers in Java
- Conversion between binary numbers and decimals
- Perform addition and subtraction on binaries

Binary Literal
- Prefix the number with oB or ob
    - Simplifies binary number usage

            @Test
            public void given_binaryLiteral_thenReturnDecimalValue() {
                byte five = 0b101;
                assertEquals((byte) 5, five);
            
                short three = 0b11;
                assertEquals((short) 3, three);

                int nine = 0B1001;
                assertEquals(9, nine);

                long twentyNine = 0B11101;
                int minusThirtySeven = -0B100101;                
            }


Binary Number Conversion
- Decimal to Binary Number
    - Integer have a functino named toBinaryString to convert a decimal number into its binary string

            @Test
            public void given_decimalNumber_then_convertToBinaryNumber(){
                assertEquals("1000", Integer.toBinaryString(8));
                assertEquals("10100", Integer.toBinaryString(20));
            }
- Binary to a Decimal Number
    - Integer class provides a parseInt function
        - Arguments: Binary String to be converted, Radisx or base of the number system in which input string has to be converted

            @Test
            public void given_binaryNumber_then_ConvertToDecimalNumber(){
                assertEquals(8, Integer.parseInt("1000", 2));
                assertEquals(20, Integer.parseInt("10100", 2));
            }

---

Arithmetic Operations
- Addition: Simply add digit by digit, remember add 1 to next digit when summing 1+1 
- Subtraction:
    - Complement Number: Negating each digit of the binary number, replace 0 to 1 and vice versa
    - There is a simpler calculation involving the complement, won't go into details