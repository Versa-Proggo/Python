string = "pneumonoultramicroscopicsilicovolcanoconiosis"
x = 5
if (type(x)is int):
    print("True")
else:
    print("False")
x = 5.0
print(type (x))
if (type(x) is not int or type(x) is not  str):
    print("True")
else:
    print("False")
x = 10
y = x * 2
print(f"Is x == y? =>{x is y} and Is x != y ? => {x is not y}")