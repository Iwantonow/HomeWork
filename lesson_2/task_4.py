# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов(n) вводится с клавиатуры.

n = int(input('Сумму скольки элементов будем считать: '))
num_list = -2
MULT_LIST = -0.5
sum = 0

while n >= 1:
    num_list = num_list * MULT_LIST
    sum = sum + num_list
    n -= 1

print(sum)


# # рекурсия
#
# def sum_num_list(a):
#     num_list = 1
#     MULT_LIST = -0.5
#     if a == 1:
#         return num_list
#     else:
#         return MULT_LIST ** (a - 1) + sum_num_list(a - 1)
#
# print(sum_num_list(n))
