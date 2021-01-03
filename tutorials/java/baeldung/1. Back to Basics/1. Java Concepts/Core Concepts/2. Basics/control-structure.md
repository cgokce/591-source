#### Control Structures

    https://www.baeldung.com/java-control-structures

- In a most basic sense, a program is a list of instructions
- Control structures are programming blocks that can change the path we take through instructions
- Three types of control structures available
- Conditional Branches -> Choosing between 2 or more paths
    - If/else/else if, ternary operator and switch
- Loops -> Iterate through multiple values/objects and repeatedly run specific code blocks
    - while, do/while, for
- Branching Statements -> Alter the flow of control in loops
    - break and continue


Conditional Branches
- If/else/else if
    - We can infinitely chain or nest it but hurts code readability, not advised in lots of nested usages
- Ternary Operator
    - Shorthand experssion that works like an if/else statement
    - Makes code more readable, but doesnt always a good substitute for if/else

            count > 2 ? "Count is higher than 2" : "Count is lower then or equal to 2";
- Switch
    - Use when we have multiple cases to choose from
    - Has some input limitations to remember when using it

        switch (count) {
            case 0:
                System.out.println("Count is equal to 0");
                break;
            case 1:
                System.out.println("Count is equal to 1");
                break;
            default:
                System.out.println("Neither 0 nor 1");
                break;
        }

Loops and Branching
- Loops: Repeat the same code multiple types in succession

        for (int i = 0; i<100; i++) {...}

        int counter = 0;
        while (counter < 50){... counter++; }

- Branching
    - Break -> Use it to exit early from a loop
    - Continue -> Skip the rest of the loop we're in
    - Handy when iterating, can often rewritten with return or other logic

---

    https://www.baeldung.com/java-using-not-in-if-conditions

Using the Not Operator
- Logical unary operator represented with ! symbol
- Works by inverting (or negating) the value of its operand
- Easier to read when we compare a condition to false

        if(!shouldBeFalse){...}

- When applying to boolean expression, **you need to surround expression in parenthesis**

        System.out.println(!true);        // Bool Value
        System.out.println(!(count > 2)); // Bool Expr

- When negating an expression, keep in mind De Morgan's law to simplify hard to read expressions

        !(a < 3 && b == 10) => a >= 3 || b != 10


Common Pitfalls of Not Operators
- Can sometimes compromies the readability of our code.
- **Negatives can be harder to read/understand than positives.**
- Double Negatives
    - Using negative variable/function name with not operator
        
        if (!product.isNotActive()){...}

        // Should better be this, more readable
        if (product.active()){...}

- Complex Conditions
    - Not operator can make already complex condition more difficult to read
    - We can simplify the code by reversing the condition or by extracting methods

            if (!(a >= b)) // Complex
            if (a < b)     // Simplified

            if (!(count >= 10) || total >= 1000)    // Complex
            if (count < 10 && total < 1000)         // Simplified
