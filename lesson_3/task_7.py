# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 10
random_list = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(random_list)
min_values = {'min_num1': random_list[0], 'min_num2': random_list[0]}

for i in random_list:
    if i < min_values['min_num1'] and i < min_values['min_num2']:
        min_values['min_num1'] = i
    if random_list.count(i) > 1 and i < min_values['min_num2']:
        min_values['min_num2'] = i
    elif i > min_values['min_num1'] and i < min_values['min_num2']:
        min_values['min_num2'] = i

if min_values['min_num1'] != min_values['min_num2']:
    print(f"Первое наименьшее число: {min_values['min_num1']}, второе наименьшее число: {min_values['min_num2']}")
else:
    print(f"Значения одинаковы и равны: {min_values['min_num1']}")