# https://stackoverflow.com/questions/12101958/how-to-keep-track-of-class-instances?noredirect=1&lq=1
#   HOW LOCALS() WORKS
#how many references on the object exists, use sys.getrefcount
import sys
class Employee:
    """Базовый класс для всех сотрудников"""
    instances = []

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.instances.append(self)

    @classmethod
    def display_count(cls):
        print('Всего сотрудников: %d' % len(Employee.instances))

    def display_employee(self):
        print('Имя: {}. Зарплата: {}'.format(self.name, self.salary))

    def delete_employee(self):
        Employee.instances.remove(self)
        del self

    def __del__(self): #del self does almost nothing -- it only deletes the local variable that is named self.
        # But as that isn't the last reference to the instance (whatever called this method also still has a reference, at least) the object will continue to exist.
        # !!! Calling __del__ manually also achieves nothing except for running that method; it doesn't delete anything.
        # print(self)
        # class_name = self.__class__.__name__
        print('{} уничтожен'.format(self.name))

emp1 = Employee("Андрей", 2000)
emp2 = Employee("Мария", 5000)
emp3 = Employee("Avonlee", 7000)
print(sys.getrefcount(emp1))
# print('Employee.__dict__:')
# print(Employee.__dict__)
# print('locals():')
# print(locals())
# print(dir(Employee))
# print(dir())
# del emp1 #Вызов del x не приводит напрямую к вызову x.__del__(), а лишь уменьшает значение счётчика ссылок на единицу.
# Описываемый метод же будет вызван, только когда счётчик ссылок достигнет нуля.
print(locals())
emp1.__del__()
print(locals())

print('+++++++++')
print()
# print(Employee.instances)
# emp1.delete_employee()
# print(locals().values())
for ins in Employee.instances:
    print(ins.name, ins)
    print(locals())
    # print(locals().values())
    print(ins in locals().values())
    print('-----')

print("Globals=",globals())
print("Locals=",locals())
