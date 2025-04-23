import math

def operator_sel():
    num_1 = int(input("Enter first number: "))
    num_2 = int(input("Enter second number: "))

    operator_func = str(input("Enter operator(+, -, **, /): "))

    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '**': lambda x, y: pow(x, y),
        '/': lambda x, y: x / y if y != 0 else 'Division by zero error'
        
    }

    result = operations.get(operator_func, lambda x, y: 'Invalid operator')(num_1, num_2)
    print("Result:", result)
        
operator_sel()