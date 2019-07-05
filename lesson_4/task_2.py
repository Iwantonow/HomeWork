import cProfile

# index_num = int(input('Какой по счету элемент будем искать: '))

def not_sieve(i):
    list_prime_num = [2]
    x = list_prime_num[0] + 1
    while len(list_prime_num) < i:
        if x % 2 == 0:
            x += 1
            continue
        else:
            root_x = int(x ** 0.5) + 1
            for num in range(2, root_x + 1):
                if x % num == 0:
                    break
            else:
                list_prime_num.append(x)
            x += 1
    return list_prime_num[i - 1]

# "task_2.not_sieve(10)"
# 100 loops, best of 5: 39.2 usec per loop
# "task_2.not_sieve(100)"
# 100 loops, best of 5: 952 usec per loop
# "task_2.not_sieve(1000)"
# 100 loops, best of 5: 20.9 msec per loop

# cProfile.run('not_sieve(10)')
# 1    0.000    0.000    0.000    0.000 task_2.py:5(not_sieve)
# 1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
# 28   0.000    0.000    0.000    0.000 {built-in method builtins.len}
# 9    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
# cProfile.run('not_sieve(100)')
# 1    0.001    0.001    0.001    0.001 task_2.py:5(not_sieve)
# 1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
# 540  0.000    0.000    0.000    0.000 {built-in method builtins.len}
# 99   0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
# cProfile.run('not_sieve(1000)')
# 1     0.022    0.022    0.023    0.023 task_2.py:5(not_sieve)
# 1     0.000    0.000    0.023    0.023 {built-in method builtins.exec}
# 7918  0.001    0.000    0.001    0.000 {built-in method builtins.len}
# 999   0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}


def sieve(n):
    list_num = [_ for _ in range(n ** 2 + 2)]
    list_num[1] = 0
    list_prime_num = []
    counter = 0
    for i in range(2, n ** 2):
        if len(list_prime_num) != n:
            if list_num[i] != 0:
                list_prime_num.append(list_num[i])
                j = i + i
                while j < n ** 2:
                    list_num[j] = 0
                    j += i
        else:
            break
    return list_prime_num[n - 1]

# "task_2.sieve(10)"
# 100 loops, best of 5: 102 usec per loop
# "task_2.sieve(100)"
# 100 loops, best of 5: 15.1 msec per loop
# "task_2.sieve(1000)"
# 100 loops, best of 5: 1.76 sec per loop


# cProfile.run('sieve(10)')
# 1    0.022    0.022    0.023    0.023 task_2.py:5(not_sieve)
# 1    0.000    0.000    0.023    0.023 {built-in method builtins.exec}
# 7918 0.001    0.000    0.001    0.000 {built-in method builtins.len}
# 999  0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
# cProfile.run('sieve(100)')
# 1    0.013    0.013    0.014    0.014 task_2.py:46(sieve)
# 1    0.001    0.001    0.001    0.001 task_2.py:47(<listcomp>)
# 1    0.000    0.000    0.014    0.014 {built-in method builtins.exec}
# 541  0.000    0.000    0.000    0.000 {built-in method builtins.len}
# 100  0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
# cProfile.run('sieve(1000)')
# 1    1.762    1.762    1.857    1.857 task_2.py:46(sieve)
# 1    0.094    0.094    0.094    0.094 task_2.py:47(<listcomp>)
# 1    0.000    0.000    1.868    1.868 {built-in method builtins.exec}
# 7919 0.001    0.000    0.001    0.000 {built-in method builtins.len}
# 1000 0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}