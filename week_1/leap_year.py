# while True:
#     year = input('Введите год: ')
#     if not year.isdigit():  # проверяет на целые числа, на дробь возвращает фолс.
#         # кстати, функции, проверяющей на дроби как на числа, нет.
#         print('Введите год правильно!')
#         continue
#
#     year = int(year)
#
#     if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#         print(year, 'год - високосный')
#         break
#     else:
#         print(year, 'год - не високосный')
#         break


import calendar
while True:
    year = input('Введите год:')
    if not year.isdigit():
        print("Введите год правильно!")
        continue

    year = int(year)
    if calendar.isleap(year):
        print(year, 'год - високосный')
        break
    else:
        print(year, 'год - не високосный')
        break
