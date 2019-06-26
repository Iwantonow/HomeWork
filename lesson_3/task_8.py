# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

SIZE_ROW = 5
SIZE_COLUMN = 3
array = [[int(input('Введите элемент матрицы: ')) for _ in range(SIZE_COLUMN)] for _ in range(SIZE_ROW)]
for row in array:
    sum_item = 0
    for item in row:
        sum_item = sum_item + item
    row.append(sum_item)
    for item in row:
        print(f'{item:>4}', end=' ')
    print()