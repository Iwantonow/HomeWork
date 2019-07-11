from collections import namedtuple

x = int(input('Сколько предприятий: '))
counter = 1
company = namedtuple('company', 'title, profit')
companys = []
average_profit = 0
while counter <= x:
    title = input('Название: ')
    quarter1 = int(input('Прибыль в 1 квартале: '))
    quarter2 = int(input('Прибыль в 2 квартале: '))
    quarter3 = int(input('Прибыль в 3 квартале: '))
    quarter4 = int(input('Прибыль в 4 квартале: '))
    profit = round((quarter1 + quarter2 + quarter3 + quarter4) / 4, 2)
    com = company(title, profit)
    companys.append(com)
    average_profit += com.profit
    counter += 1

average_profit = average_profit / x
print(f'Средняя прибыль: {average_profit}')
print('Компании с прибылью выше среднего:')
for i in range(len(companys)):
    if companys[i].profit >= average_profit:
        print(f'{companys[i].title} со редей прибылью: {companys[i].profit}')

print('Компании с прибылью ниже среднего:')
for i in range(len(companys)):
    if companys[i].profit < average_profit:
        print(f'{companys[i].title} со редей прибылью: {companys[i].profit}')