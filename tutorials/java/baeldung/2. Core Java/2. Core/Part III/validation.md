#### Java Bean Validation Basics

    https://www.baeldung.com/javax-validation

- Validating user input is a super common requirement in most applications
    - Java Bean validation framework is the standard for handling this kind of logic

JSR 380
- Specification of the Java API for bean validation, part of Java SE
- Ensures properties of a bean meet specific criteria
- This version requires Java 8 or higher

Dependencies
- Validation API: javax.validation
- Reference Implementation: org.hibernate.validator
    - Entirely seperate from the persistance aspect
- Expression Language Dependecncies: org.glassfish javax.el

Using Validation Annotations
- Example using User bean

        public class User {

            @NotNull(message="Name cannot be null")
            private String name;

            @AssertTrue
            private boolean working;

            @Size(min = 10, max = 200, message = "must be between 10 and 200 characters")
            private String aboutMe;

            @Min(value = 18, message = "Minimum age need to be 18")
            @Max(value = 150, message = "Age is maximum 150")
            private int age;

            @Email(message = "Email should be valid")
            private String email;

            ...
        }

- Other validations
    - @NotEmpty: Not null or empty, String and collections
    - @NotBlank: Applied to strings, not nulll or whitespace
    - @Positive, @PositiveOrZero, @Negative, @NegativeOrZero
    - @Past, @PastOrPresent, @Future, @FutureOrPresent validates dates

- Can be applied to elements of the collection

        List<@NotBlank String> preferences;

- Java 8 also have optional type

        private LocalDate dateOfBirth;

        public Optional<@Past LocalDate> getDateOfBirth(){
            return Optional.of(dateOfBirth);
        }

Programmatic Validation
- Spring have simple ways to trigger the validation process by just using annotations

        // Get the validator
        ValidatorFactory factory = Validation.buildDefaultValidatorFactory();
        Validator validator = factory.getValidator();

        // set up the bean values
        User user = new User();
        User.setWorking(true);
        ...

        // Validate the bean
        Set <ConstraintViolation<User>> violations = validator.validate(user);

        for (ConstraintViolations<User> violation: violations){
            log.error(violation.getMessage());
        }


