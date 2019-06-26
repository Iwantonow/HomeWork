# Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив
# со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 99
random_list = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
index_list = []
count = 0

print(random_list)
for i in random_list:
    if i % 2 == 0:
        index_list.append(count)
    count += 1

print(index_list)