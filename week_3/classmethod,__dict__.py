# https://pythonru.com/primery/primery-raboty-s-klassami-v-python#toc-4
import gc
import sys


class Employee:
    """Базовый класс для всех сотрудников"""
    emp_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emp_count += 1

    @classmethod
    def display_count(cls):
        print('Всего сотрудников: %d' % Employee.emp_count)

    def display_employee(self):
        print('Имя: {}. Зарплата: {}'.format(self.name, self.salary))

    def __del__(self): #when the code is about to end the class Employaa is no longer required and so,
# it is ready to be destroyed.Before the class Awesome is destroyed the __del__ method is called automatically.
#         print(self)
        class_name = self.__class__.__name__
        print('{} уничтожен'.format(self.name))

emp1 = Employee("Андрей", 2000)
emp2 = Employee("Мария", 5000)
emp3 = Employee("Фаина", 7000)

print(sys.getrefcount(emp2))
print(len(gc.get_referrers(emp2)))
print(gc.get_referrers(emp2))
print('----')
print(locals())
print('****----')

d = dict(globals(), **locals())
print ([ref for ref in d if d[ref] is emp2])
print(sys.getrefcount(emp2)) #getrefcount also creates a reference

print('----')
print(sys.getrefcount(emp2))

del emp2 # del statement removes a variable and its reference (not the object itself).
# This is often useful when working in Jupyter notebooks because all cell variables use the global scope.
print('====')



# emp1 = Employee("Андрей", 2000)
# # print(id(emp1))
# emp1.age = 27  # Добавит атрибут 'age'.
# # del emp1.salary удалит и на дисплей эмплои вернет ошибку
# emp2 = Employee("Мария", 5000)
# Employee.display_count()
# emp1.display_employee()
# emp2.display_employee()
# print("Всего сотрудников: %d" % Employee.emp_count)
# emp1.__del__()
# Employee.display_count()
# print('-------')
# print(hasattr(emp1, 'age'))  # возвращает true если атрибут 'age' существует
# print(getattr(emp1, 'age'))  # возвращает значение атрибута 'age', выпадает в ошибку, если атрибута нетути
# setattr(emp1, 'age', 28)  #устанавливает атрибут 'age' на 28
# # print(delattr(emp1, 'age'))  # удаляет атрибут 'age'
# print('--------')
# print("Employee.__doc__:", Employee.__doc__)
# print("Employee.__name__:", Employee.__name__)
# print("Employee.__module__:", Employee.__module__)
# print("Employee.__bases__:", Employee.__bases__)
# print("Employee.__dict__:", Employee.__dict__)
# print(emp2.__dict__)