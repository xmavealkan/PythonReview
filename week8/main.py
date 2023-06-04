# Kod yozing input sifatida list qabul qilsin va nechta juft son bulsa ushani return qilsin
def nums(number):
    counter = 0
    for n in number:
        if n % 2 == 0:
            counter =+ n
    return counter

my_list = list(range(1, 11))
counter = nums(my_list)
print(counter)
