# https://stackoverflow.com/questions/136097/what-is-the-difference-between-staticmethod-and-classmethod

class A:

    def __init__(self):
        pass

    def foo(self, x):
        print("executing foo(%s, %s)" % (self, x))

    @classmethod  # It makes it possible to call the method on the class instead of an object:
    def class_foo(cls, x):
        print("executing class_foo(%s, %s)" % (cls, x)) # With classmethods,
        # the class of the object instance is implicitly passed as the first argument instead of self.

    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)" % x)


a = A()
a.foo(1)
c2 = a.foo(2)
A.class_foo(2) # You can also call class_foo using the class. In fact, if you define something to be a classmethod,
# it is probably because you intend to call it from the class rather than from a class instance
a.class_foo(1)
a.static_foo(1)
print('---')
print(A.__dict__)  # Его задача — хранить пользовательские атрибуты. Он представляет собой dictionary,
# в котором ключом является имя_атрибута, значением, соответственно, значение_атрибута.
print(a.__dict__)
print('---')
for item_name in A.__dict__:
    item = getattr(A, item_name)
    print(item)

