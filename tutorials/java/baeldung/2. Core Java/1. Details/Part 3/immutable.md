#### Immutable Object

- Object whose internal state remains constant after it has been entirely generated
- Guarantees Public API of an immutable object guarantees us that it will behave in the same way during in whole lifetime
- Eg string API provides us replace method outputs a new string, original string doesn't change

        String name = "baeldung";
        String newName = name.replace("dung", "---");

        assertEquals("baeldung", name);
        assertEquals("bael---", name)

Final Keyword
- Variables are mutable by default meaning we can change the value they hold
- By using final keyword, java compiler will throw compile error

        final String name = "baeldung";
        name = "bael...";

Immutability in Java
- Building an immutable object guarantee its internal state won't change
- When having other object as final, we won't guarantee currency api wont change, it should be required by itself
        class Money {
            private final double amount;
            private final Currency currency;

            // ...
        }

Thread Safety
- Since internal state of an immutable object won't cahnge, we can sahre it safely among multiple threads
- Referencing immutable objects by other objects is safe, they don't have side effects since they won't change