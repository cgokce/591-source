#### Validations for Enum Types

    https://www.baeldung.com/javax-validations-enums

Validating Enums
- Most standard annotations can not be applied to enums
- Only @NotNull and @Null are available for enums

Defining an anotation to validate enum pattern
- Using @interface

        // Generate the annotation
        @Target({METHOD, FIELD, ANNOTATION_TYPE, CONSTRUCTOR, PARAMETER, TYPE_USER})
        @Retention(RUNTIME)
        @Documented
        @Constraint(validatedBy = EnumNamePatternValidator.class)
        public @interface EnumNamePattern {
            String regexp();
            String message() default "must match \"{regexp}\"";
            Class<?>[] groups() default [];
            Class<? extends Payload>[] payload() default {};
        }

        // Now we can simple add new annotation using regular expression
        @EnumNamePattern(regexp = "NEW|DEFAULT")
        private CustomerType customerType;

        // We also need to provide a validator
        public class EnumNamePatternValidator implements ConstraintValidator<EnumNamePattern, Enum<?>> {
            @Override
            public void initialize(EnumNamePattern annotation){...}

            @Override
            public boolean isValid(Enum<?> value, ConstraintValidatorContext context){...}
            
        }

Validating a Subset of an Enum
- Matching an enum with regex is not type-safe
    - Makes more sense to compare with the actual values of enum
- Cannot be made generic, so we can target a specific subset

        // Example usage of the annotation (skipping the definition)
        @CustomerTypeSubset(anyOf = {CustomerType.NEW, CustomerType.OLD})
        private CustomerType customerType;
        // Skipping the validation process
- Validating a string with value is also valid, and useful to check working with JSON
- To test all of validators, we need to set up a validator which supports newly defined annotations