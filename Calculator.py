def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a/b

print("Select the operation to be performed on the numbers:")
print("Press A to add")
print("Press S to subtract")
print("Press M to multiply")
print("Press D to divide")

while True:
    selection = input("Enter any one of these options ")
    if selection in ("a", "s", "m", "d"):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if selection == "a":
            print(add(num1, num2))
        if selection == "s":
            print(subtract(num1, num2))
        if selection == "m":
            print(multiply(num1, num2))
        if selection == "d":
            print(divide(num1, num2))
        new_calculation = input("Another calculation? ")
        if new_calculation == "no":
            break
    else:
        print("Invalid!")
    



    
    




