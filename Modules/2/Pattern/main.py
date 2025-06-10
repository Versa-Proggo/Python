num = int(input("Enetr no. of rows: "))
print("Right TRIANGLE")
for rows in range(1,num+1):
    for col in range (1,rows+1):
        print("#", end = " ")
    print()
print("Floyd’s triangle")
num = int(input("Enetr no. of rows: "))
p = 1
for rows in range(1,num+1):
    for col in range (1,rows+1):
        print(p, end = " " )
        p = p+1
    print()



