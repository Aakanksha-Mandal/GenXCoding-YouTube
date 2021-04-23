import time

#define options
option = ""
def options_menu():
    global option
    print("1. kilometers - miles")
    print("2. miles - kilometers \n")
    time.sleep(0.5)
    option = input("Please enter the number of the conversion type or quit: ")

#define kilometers to miles function
def km_mi():
    kilometers = input("Enter the distance in kilometers: ")
    while (isinstance(kilometers, int) != True and isinstance(kilometers, float) != True):
        try:
            kilometers = float(kilometers)
        except ValueError:
            print("Invalid! Please enter a valid number.")
            kilometers = input("Enter the distance in kilometers ")
    miles = kilometers / 1.609
    time.sleep(0.5)
    print(kilometers, "kilometers is", miles, "miles \n")
    time.sleep(2)

#define miles to kilometers
def mi_km():
    miles = input("Enter the distance in miles: ")
    while (isinstance(miles, int) != True and isinstance(miles, float) != True):
        try:
            miles = float(miles)
        except ValueError:
            print("Invalid! Please enter a valid number.")
            miles = input("Enter the distance in miles: ")
    kilometers = miles * 1.609
    time.sleep(0.5)
    print(miles, "miles is", kilometers, "kilometers \n")
    time.sleep(2)

#print options menu
options_menu()

#evaluate options
while (option.lower() != "quit"):
    if option == "1":
        km_mi()
    elif option == "2":
        mi_km()
    else:
        while(option.lower() != "quit"):
            print("Invalid!\n")
            time.sleep(0.25)
            break
    options_menu()

#quit
if (option.lower() == "quit"):
    print("Goodbye")
