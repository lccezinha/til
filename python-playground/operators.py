# Operators >< == !=

x = 5
y = 10

print(x, y, "x > y", x > y)
print(x, y, "x < y", x < y)
print(x, y, "x == y", x == y)
print(x, y, "x != y", x != y)

# Operators and or not

print("")
print("x and y", x and y)
print("x or y", x or y)
print("not x or y", not x and y)

# == Floats

print("Operators for Floats")
x = 1.1 + 2.2
print(x == 3.3) # > false

tolerance = 1e-5
x = 1.1 + 2.2
print(abs(x - 3.3) < tolerance)

# Bool ops with non boolean

print("\nBool ops with non boolean: ")

x = 3
type(3)
print(bool(x))
print(bool(not x))

# Selecting default values

print("\nSelect default values: ")

string = "test"
s = string or "default value"
print(s) # test

string = ""
s = string or "default value"
print(s) # default value

# Identity operations

print("\nIdentity operations:")

# is / is not to check if the objects are the same internally.

x = 1000
y = 999 + 1
print(x, y)
print(x == y) # true
print(x is y) # false
