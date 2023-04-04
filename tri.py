a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))


if (a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (a**2 + c**2 == b**2):
    print("It's a right triangle!")
else:
    print("It's not a right triangle.")
