from Calculator import Calculator


calculator = Calculator()

assert calculator.add(10, 5) == 15
assert calculator.subtract(10, 5) == 5
assert calculator.multiply(10, 5) == 50
assert calculator.divide(10, 5) == 2
