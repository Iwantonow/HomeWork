# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.
import random

SIZE = 20
MIN_ITEM = -99
MAX_ITEM = 99
random_list = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(random_list)
num_dict = {'num': MIN_ITEM, 'pos': 0}
count = 0

for i in random_list:
    if i < 0:
        if i > num_dict['num']:
            num_dict['num'] = i
            num_dict['pos'] = count
    count += 1

print(f"Наибольшее отрицательное число { num_dict['num']}, расположеное на позиции {num_dict['pos']}")