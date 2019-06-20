# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

num_user = input('Введите натуральное число: ')
num_reverse = ''

for i in num_user:
    num_reverse = i + num_reverse

print(num_reverse)

# Попытка создания рекурсии
def num_rev(a):
    if len(a) == 1:
        return a
    else:
        b = int(a) % 10
        return str(b) + num_rev(str(int(a) // 10))

print(num_rev(num_user))
