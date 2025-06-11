num = int(input("Enetr no. of rows: "))
print("Right TRIANGLE")
for rows in range(1,num+1):
    for col in range (1,rows+1):
        print("#", end = " ")
    print()
print("Vertically Flipped TRIANGLE")
for rows in range(num, 0, -1):
    for col in range(rows):
        print("#", end=" ")
    print()
print("Flipped Right TRIAANGLE")
for rows in range(1, num + 1):
    for space in range(num - rows):# I used another loop in the nested loop for spaces  (First comment)
        print(" ", end=" ")
    for col in range(rows):
        print("#", end=" ")
    print()




