import time

#define options
option = ""
def options_menu():
    global option
    print("1. kilometers - miles")
    print("2. miles - kilometers\n")
    time.sleep(0.5)
    print("3. kilograms to pounds")
    print("4. pounds to kilograms\n")
    time.sleep(0.5)
    print("5. inch to meters")
    print("6. meters to inch\n")
    time.sleep(0.5)
    option = input("Please enter the number of the conversion type or quit: ")

#define km to mi
def km_mi():
    kilometers = input("Enter the distance in kilometers: ")
    while (isinstance(kilometers, int) != True and isinstance(kilometers, float) != True):
        try:
            kilometers = float(kilometers)
        except ValueError:
            print("Invalid! Please enter a valid number.")
            kilometers = input("Enter the distance in kilometers: ")
    miles = kilometers / 1.609
    time.sleep(0.5)
    print(kilometers, "kilometers is", miles, "miles\n")
    time.sleep(2)

#define mi to km
def mi_km():
    miles = input("Enter the distance in miles: ")
    while(isinstance(miles, int) != True and isinstance(miles, float) != True):
        try:
            miles = float(miles)
        except ValueError:
            print("Invalid! Please enter a valid number.")
            miles = input("Enter the distance in miles: ")
    kilometers = miles * 1.609
    time.sleep(0.5)
    print(miles, "miles is", kilometers, "kilometers\n")
    time.sleep(2)

#define kg to lb
def kg_lb():
    kilograms = input("Enter the weight in kilograms: ")
    while(isinstance(kilograms, int) != True and isinstance(kilograms, float) != True):
        try:
            kilograms = float(kilograms)
        except ValueError:
            print("Invalid! Please enter a valid number.")
            kilograms = input("Enter the weight in kilograms: ")
    pounds = kilograms * 2.205
    time.sleep(0.5)
    print(kilograms, "kilograms is", pounds, "pounds\n")
    time.sleep(2)

#define pound to kilogram
def lb_kg():
    pounds = input("Enter the weight in kilograms: ")
    while(isinstance(pounds, int) != True and isinstance(pounds, float) != True):
        try:
            pounds = float(pounds)
        except ValueError:
            print("Invalid! Please enter a valid number.")
            pounds = input("Enter the weight in kilograms: ")
    kilograms = pounds / 2.205
    time.sleep(0.5)
    print(pounds, "pounds is", kilograms, " kilograms\n")
    time.sleep(2)

#define inch to meters
def in_m():
    inches = input("Enter the length in inches: ")
    while(isinstance(inches, int) != True and isinstance(inches, float) != True):
        try:
            inches = float(inches)
        except ValueError:
            print("Invalid! Please enter a valid number.")
            inches = input("Enter the length in inches: ")
    meters = inches / 39.37
    time.sleep(0.5)
    print(inches, "inches is", meters, "meters\n")
    time.sleep(2)

#define meters to inch
def m_in():
    meters = input("Enter the length in meters: ")
    while(isinstance(meters, int) != True and isinstance(meters, float) != True):
        try:
            meters = float(meters)
        except ValueError:
            print("Invalid! Please enter a valid number.")
            meters = input("Enter the length in meters: ")
    inches = meters * 39.37
    time.sleep(0.5)
    print(meters, "meters is", inches, "inches\n")
    time.sleep(2)

#print options menu
options_menu()

#evaluate options
while (option.lower() != "quit" and isinstance(option, str) == False):
    if option == "1":
        km_mi()
    elif option == "2":
        mi_km()
    elif option == "3":
        kg_lb()
    elif option == "4":
        lb_kg()
    elif option == "5":
        in_m()
    elif option == "6":
        m_in()
    else:
        while(isinstance(option, str) == True and option.lower() != "quit"):
            print("Invalid!")
            time.sleep(0.25)
            options_menu()

#quit
if(option.lower() == "quit"):
    print("Goodybye!")