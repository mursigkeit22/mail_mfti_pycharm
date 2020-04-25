# print(bool(12))
# print(bool(0))

# x, y = True, False
# print(x or y)
# print(y or x)
# print(x and y)

# x, y, z = True, False, True
# print(x and y or z)
# print(x and z or y)
# print(y and x or z)

# x = 12
# y = False
# print(x or y)
# print(y or x)
# print(x and y)

# x = 12
# y = 'boom'
# print(x or y) # проверяет первое и видит. что дальше можно и не проверять - ленивое
# print(y or x)
# print(x and y) # выполняет логическое выражение, пока оно имеет смысл, и печатает последнее, что там было
# print(y and x)

print(bool('something'))
print(bool(''))