def square_cir():
    side = float(input("Enter side of square: "))
    result = 4 * side
    print("Circumference of Square:", result)
def rectangle_cir():
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    result = 2 * (length + width)
    print("Circumference of Rectangle:", result)
def triangle_cir():
    a = float(input("Enter side 1: "))
    b = float(input("Enter side 2: "))
    c = float(input("Enter side 3: "))
    result = a + b + c
    print("Circumference of Triangle:", result)
def circle_cir():
    pi = float("3.14159265358979323846264338327950288419716939937510")
    radius = float(input("Enter radius: "))
    result = 2 * pi * radius
    print("Circumference of Circle:", result)
print("Select shape to find circumference:")
print("1. Square")
print("2. Rectangle")
print("3. Triangle")
print("4. Circle")
def run():
    choice = input("Enter choice (1–4): ")
    if choice == "1":
        square_cir()
    elif choice == "2":
        rectangle_cir()
    elif choice == "3":
        triangle_cir()
    elif choice == "4":
        circle_cir()
    else:
        print("Invalid choice.")
run()