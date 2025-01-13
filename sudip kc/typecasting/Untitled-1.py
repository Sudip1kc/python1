
x = 10       # Integer
y = 2.5      # Float
result = x + y  # x is implicitly converted to float
print(result)   # Output: 12.5
print(type(result))  # Output: <class 'float'>

s = "Python"
print(s.upper())  # Output: PYTHON\      # Output: P
print(s + " sudip")  # Concatenation: "Python Rocks!"
my_list = [1, 2, 3, 4, 5]
mixed_list = [1, "Python", 3.14]
my_list.append(6)       # Adds an item: [1, 2, 3, 4, 5, 6]
my_list[0] = 0          # Modify: [0, 2, 3, 4, 5, 6]
print(my_list[1:4])     # Slicing: [2, 3, 4]
my_list.append('sudip')
a={1, 2, 3, 4, 5, 6}
print(a)
a="123445"
a_int=int(a)
print(type(a_int))

print(type(a))
a_float=float(a)
print(a_float)
print(type(a_float))
a=[1,2,3,4]
a_tuple=tuple(a)
print(a_tuple)
print(type(a_tuple))
