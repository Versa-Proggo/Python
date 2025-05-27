print(f"Basic For Loop and rnage function")
for i in range (1,11,2):
    print(f"For i={i}, Python  For loop")
print("basic for loop & range function for a reverse order")
for i in range (10,0,-5):
    print(f"For i={i}, Python  For loop")
print("traversing a string using for loop")
text = "Python"
for i in text:
    print(i)
print("reversing a string")
for i in range(len(text)-1,-1,-1):
    print(text [i])
n = int(input("Enter a number"))
sum = 0
for i in range(1,n):
    sum += i 
    print(f"Sum till i = {i}, sum = {sum}")
    print(f"Sum till n = {n}, sum = {sum}")