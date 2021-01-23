#### Java Switch Statement

- Allows us to replace several nested if-else constructs and improve the readability
- Improved over time, new supported types hav ebeen added

Example use
- Improving readability

        if (animal.equals("DOG")){
            ...
        }else if ...

        // Same statement as above
        switch(animal){
            case "DOG":
                result = "its a dog";
                break;
            case...
            default:
                result = "unknown animal";
                break;
        }

Break Statement
- If we do not use break, blocks underneath will be executed
    - It is essential to use breaks to exit the switch block
- We can omit break when we want the same code executed for several cases

        case "DOG":
        case "CAT":
            result = "domestic animal";
            break;
        case ...

Switch Case Values
- Data Types
    - Switch works for following primitives and wrappers
        - byte/Byte, short/Short, int/Integer, char/Character
    - Also works for enum and String
- We cant pass the null value as an argument, will result in NullPointerException
- If we want to compare to a variable, it must be final declared with final

        final String dog="DOG";

        switch(animal){
            case dog:
            ...
        }
- Switch operator uses equals() method under the hood


New Switch Expression (JDK 12 and above)
- Comma delimited values, expressive syntax

        var result = switch(month){
            case JANUARY, JUNE -> 3;
            case FEBRUARY, SEPTEMBER, OCTOBER ->1;
            ...
            default -> 0;
        }

- We can also use anonymous block statements and keyword yield

        case MARCH, MAY -> {
            int monthLength = month.toString().length();
            yield monthLength * 4;
        }

- For switch expression, compiler requires to cover all enum cases if there is no default case
- Switch is a good candidate when we have a limited number of options in a pre-defined set
    - Otherwise we'd have to modify the code each time a new value is added or removed
    - For these cases, we should consider other approaches eg. polymorphism or command pattern