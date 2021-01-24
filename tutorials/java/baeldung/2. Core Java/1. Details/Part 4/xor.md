#### Java XOR Operator

    https://www.baeldung.com/java-xor-operator

The XOR Operator
- Exclusive or (XOR) returns true if and only if operands are different
    - Equivalent to (A AND !B) OR (!A AND B)

        A B -> A XOR B
        0 0       0
        0 1       1 
        1 0       1
        1 1       0

How to do it in Java
- It can be possible to write using and or operators
- XOR operator represented by ^ symbol, and bitwise operator
- Works with every primitive type

        Car car = Car.dieselAndManualCar();
        boolean dieselXorManul = car.isDiesel() ^ car.isManual();


 