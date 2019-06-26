# Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random

SIZE_ROW = 5
SIZE_COLUMN = 4
MIN_ITEM = 0
MAX_ITEM = 20
array = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_COLUMN)] for _ in range(SIZE_ROW)]
min_column = array[0]

for row in array:
    for i, item in enumerate(row):
        if item < min_column[i]:
            min_column[i] = item

column_max_item = min_column[0]
for item in min_column:
    if item > column_max_item:
        column_max_item = item


for row in array:
    for item in row:
        print(f'{item:>4}', end=' ')
    print()
print('*' * 20)
for item in min_column:
    print(f'{item:>4}', end=' ')
print()
print('*' * 20)
print(f'Максимальный элемент среди минимальных элементов столбцов матрицы: {column_max_item}')