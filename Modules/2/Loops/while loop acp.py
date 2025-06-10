count = 0
print("Enter characters one by one (type 'stop' to end):")
while True:
    user_input = input("Enter something: ")
    if user_input.lower() == 'stop':
        break
    for charecter in user_input:
        if charecter.isdigit():
            count += 1
print("Total number of digits entered:", count)
