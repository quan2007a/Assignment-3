smallest = None
largest = None

text = input("Nhap so: ")

while text != "":
    number = float(text)

    if smallest is None:
        smallest = number
        largest = number
    else:
        if number < smallest:
            smallest = number
        if number > largest:
            largest = number

    text = input("Nhap so: ")

print("So nho nhat:", smallest)
print("So lon nhat:", largest)
