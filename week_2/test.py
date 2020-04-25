# class StrWithFours:
#     #four = '4'
#
#     def __init__(self, mystr='4'):  # в классе обязательно должен быть метод. Метод - это функция,
#         # описанная внутри класса
#         # self  - именно тот объект класса, с которым мы сейчас работаем
#         self.mystr = mystr
#     def __withfours__(self, mystr):
#
#
# a = StrWithFours("ama")
# b = StrWithFours()
# print(a.mystr)
# print(b.mystr)
# print(a, b)
# d = {'d':4}
# print(type(d))
# a = dict(hop=1, op=2)
# c = 'hop'
# print(hash(c))   # every time hash is different
# int_c = int(1)
# float_c = float(1.0)
# print(hash(int_c))
# print(hash(float_c))
# print(hash(1))

import sys
import struct
import ctypes
obj = 1
print(sys.version)
print(sys.getsizeof(obj), obj.__sizeof__()    )
# print(ctypes.string_at(id(obj), 14)   )
# print(ctypes.string_at(id(obj), 28)   )
#
# print(struct.unpack('lll', ctypes.string_at(id(obj), 12)) )
# print(struct.unpack('LLl', ctypes.string_at(id(obj), 12)) )
#
# print(struct.unpack('lllllll', ctypes.string_at(id(obj), 28)) )
# print('----')
# l = 4,
# L = 4,
# N = 8,
# n = 8,
# q = 8,
# Q = 8,
# P = 8,
# d = 8,
# c = 1,
# x = 1,
# ? = 1
print(struct.unpack('l', ctypes.string_at(id(obj), 4)) )
print(struct.unpack('L', ctypes.string_at(id(obj), 4)) )
print(struct.unpack('N', ctypes.string_at(id(obj), 4)) )
print(struct.unpack('P', ctypes.string_at(id(obj), 4)) )
print(struct.unpack('Q', ctypes.string_at(id(obj), 8)) )
print(struct.unpack('n', ctypes.string_at(id(obj), 4))  )
print(struct.unpack('?', ctypes.string_at(id(obj), 1)) )
print(struct.unpack('d', ctypes.string_at(id(obj), 8)) )






# print(help(struct))

 # 28 # (142, 1696001384, 1, 1, 93, 1696001384, 1)
