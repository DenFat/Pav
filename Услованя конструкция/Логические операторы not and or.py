# Логический оператор end
#
# print(10 > 0 and 5 > 0)  # Вернет True
# print(10 % 2 == 0 and 12 % 2 == 0)  # Вернет True
# print('ма' in 'мама мыла раму' and 5 > 0)  # Вернет True
#
# print(10 > 0 and 5 > 0)  # Вернет True
# print(10 % 2 == 0 and 12 % 2 == 0)  # Вернет True
# print('ма' in 'мама мыла раму' and 5 > 0)  # Вернет True

# day = 3
# if (day >= 0) and (day <= 5):
#     print('Число входит в диапазон')

# python  = 'питон'
# coffe = 'кофе'
# cat = 'кот'
#
# # result = len(python) < 5 and len(coffe) and len(cat) < 5
# result = len(python) < 5 or len(coffe) < 5 or len(cat) < 5
# print(result)

# a = int(input())
# b = 4
# c = 3
# v = a > b or b == 2
# print(v)

# Логический оператор not
# print(not False)

# x = 0
# if not x:
#     print('x не равно нулю')
# else:
#     print('x равно нулю')

# my_string = ''
# if not my_string:
#     print('Строка пустая')
# else:
#     print('Строка не пустая')

# a = int(input())
# b = int(input())
#
# c = a * b
# if c % 2 == 0 or \
#     c % 3 == 0 or \
#     c % 4 == 0 or \
#     c % 5 == 0:
#
#     print('Произведение кратно 2 или 3 или 4 или 5')