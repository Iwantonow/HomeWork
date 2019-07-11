from collections import deque

def sum_num(a, b):
    num1 = a.copy()
    num2 = b.copy()
    num_dic = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
    }
    letter_dic = {
        0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
        10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F',
    }
    counter = 0
    result_sum = deque()

    while True:
        if len(num1) < len(num2):
            num1.appendleft('0')
        elif len(num1) > len(num2):
            num2.appendleft('0')
        else:
            break

    for i in range(len(num1) - 1, -1, -1):
        res = num_dic[num1[i]] + num_dic[num2[i]] + counter
        counter = 0
        if res > 15:
            counter += res // 16
            res = res - 16 * counter
        result_sum.appendleft(letter_dic[res])
    if counter != 0:
        result_sum.appendleft(letter_dic[counter])
    return result_sum

def mult_num(a, b):
    num1 = a.copy()
    num1.reverse()
    num2 = b.copy()
    num2.reverse()

    num_dic = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
    }
    letter_dic = {
        0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
        10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F',
    }

    counter = 0
    count = 0
    list_mult = []
    mult = deque()

    for i in num2:
        for j in num1:
            res = num_dic[i] * num_dic[j] + counter
            counter = 0
            if res > 15:
                counter += res // 16
                res = res - 16 * counter
            mult.appendleft(letter_dic[res])
        if counter != 0:
            mult.appendleft(letter_dic[counter])
        for _ in range(count):
            mult.append('0')
        list_mult.append(mult)
        mult = deque()
        count += 1
        counter = 0

    for i in range(len(list_mult) - 1):
        if i == 0:
            res_sum = sum_num(list_mult[i], list_mult[i + 1])
        else:
            res_sum = sum_num(res_sum, list_mult[i + 1])
    return res_sum



x = deque(input('Введите первое число: ').upper())
y = deque(input('Введите второе число: ').upper())

print('Сумма: ', end='')
for i in sum_num(x, y):
    print(i, end='')
print()

print('Произведение: ', end='')
for i in mult_num(x, y):
    print(i, end='')

