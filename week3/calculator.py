# create your settings
def add(x, y):
    return x + y
def subtraction(x, y):
    return x - y
def multiplication(x, y):
    return x * y
def devide (x, y):
    return x / y

print("plese enter number")
 

num1 = int(input("Enter the first number"))

choice = input("Select operation + - * /:")

num2 = int(input("Enter the second number"))

# Execute the selected operation

if choice == "+":
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == "-":
    print(num1, "-", num2, '=', subtraction(num1, num2))
elif choice == "*":
    print(num1, '*', num2, '=', multiplication(num1, num2))
elif choice == '/':
    print(num1, '/', num2, '=', devide(num1, num2))
else:
    print("Invalid operation selection")


    
