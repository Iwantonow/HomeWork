# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random

SIZE = 30
MIN_ITEM = 0
MAX_ITEM = 99
random_list = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(random_list)
min_max_values = {'min_num': random_list[0], 'min_pos': 0, 'max_num': random_list[0], 'max_pos': 0}
count = 0
sum_item = 0

for i in random_list:
    if i < min_max_values['min_num']:
        min_max_values['min_num'] = i
        min_max_values['min_pos'] = count
    elif i > min_max_values['max_num']:
        min_max_values['max_num'] = i
        min_max_values['max_pos'] = count
    count += 1

# Подскажите как избавиться от повторения кода в данной ситуации если нельзя использовать
# даже самостоятельно написанные функции?
if min_max_values['min_pos'] < min_max_values['max_pos']:
    for i in random_list[min_max_values['min_pos'] + 1: min_max_values['max_pos']]:
        sum_item = sum_item + i
else:
    for i in random_list[min_max_values['max_pos'] + 1: min_max_values['min_pos']]:
        sum_item = sum_item + i
print(sum_item)