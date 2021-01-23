#### Modulo operator in Java

    https://www.baeldung.com/modulo-java

Division
- In Java, if operands on both sides of the division hav tyoe int, result would be another int
    - If one of them were float or double we would get float/double result

        assertThat(11/4).isEqualTo(2);
        assertThat(11/4.0).isEqualTo(2.75);
- Modulo operator results in remainder, thus saving remainder of integer division which otherwise lost

        assertThat(11%4).isEqualTo(3);        
- If right side is 0 in division we'll get arighmeticException 

Common Modulo Usage
- We can find out if a given number is odd or even.
- Keep track of the index of the next free spot in a circular array
    - This way we'll never get the ArrayIndexOutOfBoundsException

