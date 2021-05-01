class MyClass:
    def method(self):
        """
        Can modify object instance state
        Can modify class state
        """
        return "Instance method called", self

    @classmethod
    def classmethod(cls):
        """
        Can not modify object instance state
        Can modify class state
        Does not access self
        """
        return "Class method called", cls

    @staticmethod
    def staticmethod():
        """
        Can not modify object instance state
        Can not modify class state
        """
        return "Static method called"


my_class = MyClass()
print(my_class.method())
print(my_class.classmethod())
print(my_class.staticmethod())
print("\n--\n")
print(MyClass.classmethod())
print(MyClass.staticmethod())
