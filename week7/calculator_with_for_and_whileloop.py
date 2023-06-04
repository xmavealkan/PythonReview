def add(x,y):
    return x + y
def minus (x,y):
    return x - y
def multiplication(x, y):
    return x * y
def devide(x,y):
    if y == 0:
        return 'zero is not devided'
    else:
        return x / y

def choice(oplist):
    
    result = []
    
    for n in oplist:
        result.append(n)
    return result

my_operation_list = ['+', '-', '*', '/']
result = choice(my_operation_list)

while True:
    choice_operation = input("enter the operatoin: ")
    nums_list = []
    
    if choice_operation in result:
        num1 = float(input("enter the  first number: "))
        num2 = float(input("enter the second number: "))
        
        if choice_operation == "+":
            print(num1, '+', num2, '=' , add(num1, num2))   
        elif choice_operation == "+":
            print(num1, '-', num2, '=' , add(num1, num2)) 
        elif choice_operation == '*':
            print(num1, '*', num2, '=', multiplication(num1, num2))  
        elif choice_operation == '/':
            print(num1, '/', num2, '=', multiplication(num1, num2))  
    elif choice_operation == 'quit':
        print('goodbye know we are always ready to help you')
        break
    else:
        print("invalid operation")










