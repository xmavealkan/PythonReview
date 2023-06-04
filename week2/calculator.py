# Функция для сложения двух чисел
def add(x, y):
    return x + y

# Функция для вычитания двух чисел
def subtract(x, y):
    return x - y

# Функция для умножения двух чисел
def multiply(x, y):
    return x * y

# Функция для деления двух чисел
def divide(x, y):
    return x / y

# Выводим меню для выбора операции
print("Выберите операцию:")
print("+")
print("-")
print("*")
print("/")

# Запрашиваем у пользователя выбор операции
choice = input("напиши операцию: ")

# Запрашиваем у пользователя два числа
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

# Выполняем выбранную операцию
if choice == '+':
    print(num1, "+", num2, "=", add(num1, num2))

elif choice == '-':
    print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == '*':
    print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == '/':
    print(num1, "/", num2, "=", divide(num1, num2))

else:
    print("Неверный выбор операции")
