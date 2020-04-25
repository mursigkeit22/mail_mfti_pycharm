#https://rushter.com/blog/python-garbage-collector/
import sys

foo = []

# 2 references, 1 from the foo var and 1 from getrefcount
print("hop 1")
print(sys.getrefcount(foo))


def bar(a):
    # 4 references
    # from the foo var, function argument, getrefcount and Python's function stack
    print("hop 2")

    print(sys.getrefcount(a))


bar(foo)
print('hop 3')
# 2 references, the function scope is destroyed
print(sys.getrefcount(foo))