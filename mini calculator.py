def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except :
        return "ERROR: Cannot divide by zero"

def rem(x, y):
    return x % y

print("------ MINI CALCULATOR ------")

while True:
    print("\nSELECT AN OPERATION")
    print("1. ADD")
    print("2. SUBTRACT")
    print("3. MULTIPLY")
    print("4. DIVIDE")
    print("5. REMAINDER")
    print("6. QUIT")

    choice = input("ENTER YOUR CHOICE (1-6): ")

    if choice == '6':
        print("THIS PROGRAM IS TERMINATED")
        break

    if choice in ['1', '2', '3', '4', '5']:
        try:
            a = float(input("ENTER FIRST NUMBER: "))
            b = float(input("ENTER SECOND NUMBER: "))
        except ValueError:
            print("INVALID INPUT: Please enter numeric values.")
            continue

        if choice == '1':
            print("RESULT:", add(a, b))
        elif choice == '2':
            print("RESULT:", subtract(a, b))
        elif choice == '3':
            print("RESULT:", multiply(a, b))
        elif choice == '4':
            print("RESULT:", divide(a, b))
        elif choice == '5':
            print("RESULT:", rem(a, b))
    else:
        print("INVALID CHOICE. PLEASE SELECT FROM 1 TO 6.")
