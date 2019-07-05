# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.
import cProfile

# конкатенация
def num_reverse(a):
    num_reverse = ''
    for i in a:
        num_reverse = i + num_reverse
    return num_reverse
# "task_1.num_reverse('1' * 1000)"
# 100 loops, best of 5: 276 usec per loop
# "task_1.num_reverse('1' * 10000)"
# 100 loops, best of 5: 6 msec per loop
# "task_1.num_reverse('1' * 100000)"
# 100 loops, best of 5: 330 msec per loop

# cProfile.run('num_reverse("1" * 1000)')
# 1    0.000    0.000    0.000    0.000 task_1.py:8(num_reverse)
# cProfile.run('num_reverse("1" * 10000)')
# 1    0.007    0.007    0.007    0.007 task_1.py:8(num_reverse)
# cProfile.run('num_reverse("1" * 100000)')
# 1    1.023    1.023    1.023    1.023 task_1.py:8(num_reverse)



def num_r(a):
    a = a[::-1]
    return a
# "task_1.num_r('1' * 1000)"
# 100 loops, best of 5: 3.9 usec per loop
#  "task_1 "task_1.num_r('1' * 10000)"
# 100 loops, best of 5: 33.2 usec per loop
#  "task_1.num_r('1' * 100000)"
# 100 loops, best of 5: 517 usec per loop

# cProfile.run('num_r("1" * 1000)')
# 1    0.000    0.000    0.000    0.000 task_1.py:27(num_r)
# cProfile.run('num_r("1" * 10000)')
# 1    0.000    0.000    0.000    0.000 task_1.py:27(num_r)
# cProfile.run('num_r("1" * 100000)')
# 1    0.000    0.000    0.000    0.000 task_1.py:27(num_r)


# рекурсия с конкатенацией
def num_rev(a):
    if len(a) == 1:
        return a
    else:
        b = int(a) % 10
        return str(b) + num_rev(str(int(a) // 10))
#  "task_1.num_rev('1' * 100)"
# 100 loops, best of 5: 392 usec per loop
# "task_1.num_rev('1' * 300)"
# 100 loops, best of 5: 3.31 msec per loop
# "task_1.num_rev('1' * 600)"
# 100 loops, best of 5: 18.4 msec per loop
# "task_1.num_rev('1' * 990)"
# 100 loops, best of 5: 71.5 msec per loop

# cProfile.run('num_rev("1" * 100)')
# 100/1    0.001    0.000    0.001    0.001 task_1.py:35(num_rev)
# cProfile.run('num_rev("1" * 300)')
# 300/1    0.004    0.000    0.004    0.004 task_1.py:35(num_rev)
# cProfile.run('num_rev("1" * 600)')
# 600/1    0.020    0.000    0.020    0.020 task_1.py:35(num_rev)
# cProfile.run('num_rev("1" * 990)')
# 990/1    0.074    0.000    0.074    0.074 task_1.py:35(num_rev)





# рекурсия без конкатенации
def num_rev_int(a):
    a = int(a)
    if a // 10 == 0:
        return f'{a}'
    b = a % 10
    return f'{b}{num_rev_int(a // 10)}'
#  "task_1.num_rev_int('1' * 100)"
# 100 loops, best of 5: 167 usec per loop
# "task_1.num_rev_int('1' * 300)"
# 100 loops, best of 5: 760 usec per loop
#  "task_1.num_rev_int('1' * 600)"
# 100 loops, best of 5: 2.29 msec per loop
# "task_1.num_rev_int('1' * 990)"
# 100 loops, best of 5: 5.67 msec per loop

# cProfile.run('num_rev_int("1" * 100)')
# 100/1    0.000    0.000    0.000    0.000 task_1.py:64(num_rev_int)
# cProfile.run('num_rev_int("1" * 300)')
# 300/1    0.001    0.000    0.001    0.001 task_1.py:64(num_rev_int)
# cProfile.run('num_rev_int("1" * 600)')
# 600/1    0.003    0.000    0.003    0.003 task_1.py:64(num_rev_int)
# cProfile.run('num_rev_int("1" * 990)')
# 990/1    0.008    0.000    0.008    0.008 task_1.py:64(num_rev_int)


# Вывод:
# Среди предложенных вариантов решения с использованием конкатенации строк значительно уступают
# по времени выполнения кода свои аналогам, в то же время рекурсии сильно отстают даже от цикла.
# Лучшим вариантом по быстродействию является срез.
#
# попробую предположить сложность моих функций:
# цикл: O(n) * 2 (2 - это конкатенация)
# срез: O(n)
# рекурсия с конкатенацией: O(n) * 2 * x (где x - количество вызовов рекурсии и 2 - это конкатенация)
# рекурсия: O(n) * x (x - количество вызовов рекурсии)