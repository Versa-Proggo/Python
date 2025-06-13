def add(a,b):
    return a+b
def sub (a,b):
    return a-b
def mul (a,b):
    return a*b
def divide (a,b):
    return a/b
def module(a,b):
    return(a%b)
def exponent (a,b):
    return (a**b)
def sim_cal(a,b,op):

    if op == "+":
        print(f"{a} +{b} = {add(a,b)}")
    elif op == "-":
        print(f"{a} -{b} = {sub(a,b)}")
    elif op == "*":
        print(f"{a} x {b} = {mul(a,b)}")
    elif op == "/":
        print(f"{a} / {b} = {divide(a,b)}")
    elif op == "**":
        print(f"{a} ** {b} = {exponent(a,b)}")
    elif op == '%':
        print(f"{a} % {b} = {module(a,b)}")
    else:
        print('You gave the wrong operater, Rerun me')
a = int(input("Enter 1st no.: ")) 
b = int(input("Enter 1st no.: "))
op = input("Enter operater (+,-,x,/,**,%): ")
sim_cal(a,b,op)


    