
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error"
    return a / b

print("Addition:", add(3, 2))
print("Subtraction:", subtract(5, 2))
print("Multiplication:", multiply(4, 2))
print("Division:", divide(10, 2))
print("Division by zero:", divide(5, 0))