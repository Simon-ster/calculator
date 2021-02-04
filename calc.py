
def add(a,b):
    return a + b

def multiply(a,b):
    return round(a * b,3)

def subtract(a,b):
    return a - b

def divide(a,b):
    if b != 0:
        return float(a) / float(b)
    else:
        raise ZeroDivisionError
        print("Cannot divide by zero")

if __name__ == '__main__':
    while True:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))

        print("addition: " + str(add(a,b)))
        print("multiplication: " + str(multiply(a,b)))
        print("subtraction: " + str(subtract(a,b)))
        print("division: " + str(divide(a,b)))