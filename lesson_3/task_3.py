# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 99
random_list = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(random_list)
min_max_values = {'min_num': random_list[0], 'min_pos': 0, 'max_num': random_list[0], 'max_pos': 0}
count = 0

for i in random_list:
    if i < min_max_values['min_num']:
        min_max_values['min_num'] = i
        min_max_values['min_pos'] = count
    elif i > min_max_values['max_num']:
        min_max_values['max_num'] = i
        min_max_values['max_pos'] = count
    count += 1

random_list[min_max_values['min_pos']] = min_max_values['max_num']
random_list[min_max_values['max_pos']] = min_max_values['min_num']
print(random_list)