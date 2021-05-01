class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 22
        self.__xunda = 33

t = Test()
print(t)
print(t.foo) # > 11
print(t._bar) # > 22
# print(t.__xunda) # AttributeError: 'Test' object has no attribute '__xunda'

print(dir(t))

# ['_Test__xunda', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__',
#     '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_bar', 'foo']

# _bar = kind a convencion/hint to allow programmers to understand that this is a private variable and should take care when changing it.
# __xunda turns into _Test__xunda on dir(t), it protected subclasses from Test to use the same variable name