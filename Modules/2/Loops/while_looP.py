for i in range (1,11,2):
    print(f"{i}", end=", ")
x = 1
while(x<11):
    print(f"{x}" ", ")
    x+=1

n = int(input(f"Enter a number till when u wanna find the sum of "))
p = 0
sum = 0
while(p <= n):
    sum += p 
    print(f"Sum till {p} = {sum}")
    p += 1 
print(f"Total Sum = {sum}")

x = int(input(f"enter a number"))
x_l = len(str(x))
p = 0
temp = x
while(temp>0):
    digit = temp % 10
    print(f"No of digits in {x} is {digit}")
    p+= digit**3
    temp//= 10
    
if sum == x:
    print(f"{x} is an Armstrog Number")
else:
    print(f"{x} is not an  Armstrog Number")