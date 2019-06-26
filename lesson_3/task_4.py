# Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 30
MIN_ITEM = 0
MAX_ITEM = 9
random_list = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(random_list)
num_dict = {'num': 0, 'pos': 0, 'rec': 0}
num_list = []
count = 0

for i in random_list:
    if i not in num_list:
        if random_list.count(i) > num_dict['rec']:
            num_dict['num'] = i
            num_dict['pos'] = count
            num_dict['rec'] = random_list.count(i)
        num_list.append(i)
    count += 1

print(f"Число { num_dict['num']}, расположеное на позиции {num_dict['pos']}, встречается чаще всего, повторений: {num_dict['rec']}")