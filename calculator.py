# This is a simple calculator which add, subtracts, multiplies, and divides the two numbers given by the user.
import time

# Welcome message
print("Welcome to the Simple Calculator.")
time.sleep(1)

#define add function
def add(first, second):
    sum = first + second
    return sum

#define subtract function
def subtract(first, second):
    difference = first - second
    return difference

#define multiply fuction
def multiply(first, second):
    product = first * second
    return product

#define divide function
def divide(first, second):
    quotient = first / second
    return quotient

while (True):
    #ask user for the first number
    first = input("Please enter the first number or quit: ")
    
    #check first's data type
    def data_type(first):
        try:
            first = float(first)
            return True
        except ValueError:
            return False

    #quit
    if (data_type(first) == False and first.lower() == "quit"):
        print("Goodbye!")
        break

    #operation and second number
    elif (data_type(first) == True):
        first = float(first)

        operation = input("Please enter the operation (+, -, *, /): ")
        while (operation != "+" and operation != "-" and operation != "*" and operation != "/"):  
            print("Sorry, operation not recognized!")
            operation = input("Please enter the operation (+, -, *, /): ")

        second = input("Please enter the second number: ")
        #check second's data type
        def data_type2(second):
            try:
                second = float(second)
                return True
            except ValueError:
                return False
        
        if (data_type2(second) == True):
            second = float(second)
            print("Calculating... ")
            time.sleep(1)
        else:
            print("Invalid!")
            second = input("Please enter the second number: ")

        #print the results
        #add
        if operation == "+":
            print(first, "+", second, "=", add(first, second), "\n")
            time.sleep(1)
        
        #subtract
        elif operation == "-":
            print(first, "-", second, "=", subtract(first, second), "\n")
            time.sleep(1)

        #mutlipy
        elif operation == "*":
            print(first, "*", second, "=", multiply(first, second), "\n")
            time.sleep(1)

        #divide
        elif operation == "/":
            print(first, "/", second, "=", divide(first, second), "\n")
            time.sleep(1)
    else:
        print("Invalid!")