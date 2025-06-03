# lower = int(input(f"Enter the lower range: "))
# upper = int(input(f"Enter the upper range: "))
# print(f"Prime numbers between{lower} and {upper} are:")
# for num in range(lower,upper+1):
#     if num > 1:
#         for i in range(2,num):
#             if (num%i == 0):
#                 break
#         else:
#             print(num,end=", ")
num = int(input("Enter the number of rows"))
for i in range(1,num+1):
    for j in range(1,num+1):
        print("*",end = " ")
    print()