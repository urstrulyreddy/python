filename1 = input("Enter the name of the first file: ")
filename2 = input("Enter the name of the second file: ")

with open(filename1, "r") as f1, open(filename2, "w") as f2:
    f2.write(f1.read())

print("File contents copied successfully!")
