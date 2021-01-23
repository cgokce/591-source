#### Java toString() Method

    https://www.baeldung.com/java-tostring

- Every class in Java is a child of the Object class either directly or indirectly
    - Since Object class contains a toString() method we can call it on any instance

Default Behavior
- Whenever we print an object reference, it invokes toString() method
- Object's default toString method prints its fully qualified name and hashcode

        public String toString(){
            return getClass().getName() + "@" + Integer.toHexString(hashCode());
        }

        public class Customer{...}

        System.out.println(myCustomer)
        // com.baeldung.tostring.Customer@3sajhd4

Overriding Default Behavior
- Generally we are interested the content of our object rather than its hashcode
- Primitive Types and Strings

        @Override
        public String toString(){
            return "Customer balance:" + balance + ", firstName=" + getFirstName(); 
        }

- Complex Java Objects
    - Assume a scenario customer also contains an order attribute that is of type order
    - Order class have both string an dprimitive fields
    - Since order is a complex object, it will return the order's toString()
        - We can also override order's toString() to get desired result
- Array of Objects
    - We can use Arrays.toString() for easy string conversion

            @Override
            public String toString(){
                return "Customer class orders=" + Arrays.toString(orders);
            }
- Wrappers, Collections and StringBuffers
    - There is already a toString() implementation for those

            # Wrapper, Collection, Buffer
            eg. Integer, List<String>, StringBuffer

        