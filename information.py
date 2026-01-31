username = "python"
password = "rules"

count = 0

while count < 5:
    user = input("Nhap username: ")
    pw = input("Nhap password: ")

    if user == username and pw == password:
        print("Welcome")
        break
    else:
        print("Sai, nhap lai")
        count = count + 1

if count == 5:
    print("Access denied")
