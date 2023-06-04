def add(x, y):
    return x + y
def subtraction(x, y):
    return x - y
def multiplication(x, y):
    return x * y
def devide (x, y):
    if y == 0:
        return "zero is not devided"
    else:
       return x / y

while True:
    choice = input("enter choice:")

    
    if choice in ('+', '-', '*', '/'):
        num1 = float(input("enter first number: "))
        num2 = float(input("enter second number: "))
        
        if choice == "+":
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == "-":
            print(num1, "-", num2, '=', subtraction(num1, num2))
        elif choice == "*":
            print(num1, '*', num2, '=', multiplication(num1, num2))
        elif choice == '/':
            print(num1, '/', num2, '=', devide(num1, num2))
    elif choice == "quit":
        print("Goodbye")
        break
    else:
        print("Invalid operation selection")