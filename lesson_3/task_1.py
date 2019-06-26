# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

min_item = 2
MAX_ITEM = 99

while min_item < 10:
    print(f'в диапазоне от 2 до 99 {len([i for i in range(min_item, MAX_ITEM, min_item)])} чисел(а) кратно {min_item}')
    min_item += 1



