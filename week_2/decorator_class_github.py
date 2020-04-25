def constructor(type_):
    def decorator(method):
        method.constructs_type = type_
        return method
    return decorator

# @register_constructors
class IntStore(object):
    # constructors = {}

    def __init__(self, value):
        self.value = value

    @classmethod
    @constructor(int)
    def from_int(cls, x):
        return cls(x)

print(IntStore.from_int(1).value)