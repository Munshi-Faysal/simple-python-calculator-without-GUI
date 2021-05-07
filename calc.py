def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y
print("\n\n")
print("***Welcome to My Calculator***")

print("--> This Calculator is Calculating only for two Numbers <--")
print("\n\n")
name = input("Enter Your Name: ")

print("\n")
print(f"\tHey {name} Select operation.\n")
print("\t\tFor Addition Type 1")
print("\t\tFor Subtraction Type 2")
print("\t\tFor Multiplication Type 3")
print("\t\tFor Division Type 4\n")

while True:
    print("\n")
    choice = input("Enter choice (1 / 2 / 3 / 4): ")
    print("\n")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number : "))
        num2 = float(input("Enter second number: "))
        print("Now Calculating.......")
        print("\n")

        if choice == '1':
            print("\t",num1, "+", num2, "=", add(num1, num2))
            print("\n")
            print(f"The result of Addition is : {add(num1, num2)}")
            print("\n")
            print("Do you want to do calculate again?")
            ans = input("Enter YES/NO: ")
            if ans == 'YES':
                continue
            else:
                print("\n")
                print(f"Thank You {name}")
                print("\n\n")
                break

        elif choice == '2':
            print("\t",num1, "-", num2, "=", subtract(num1, num2))
            print("\n")
            print(f"The result of Subtraction is : {subtract(num1, num2)}")
            print("\n")
            print("Do you want to do calculate again? YES / NO ?")
            ans = input("Enter YES/NO: ")
            if ans == 'YES':
                continue
            else:
                print("\n")
                print(f"Thank You {name}")
                print("\n\n")
                break

        elif choice == '3':
            print("\t",num1, "*", num2, "=", multiply(num1, num2))
            print("\n")
            print(f"The result of Multiplication is : {multiply(num1, num2)}")
            print("\n")
            print("Do you want to do calculate again? YES / NO ?")
            ans = input("Enter YES/NO: ")
            if ans == 'YES':
                continue
            else:
                print("\n")
                print(f"Thank You {name}")
                print("\n\n")
                break

        elif choice == '4':
            print("\t",num1, "/", num2, "=", divide(num1, num2))
            print("\n")
            print(f"The result of Division is : {divide(num1, num2)}")
            print("\n")
            print("Do you want to do calculate again? YES / NO ?")
            ans = input("Enter YES/NO: ")
            if ans == 'YES':
                continue
            else:
                print("\n")
                print(f"Thank You {name}")
                print("\n\n")
                break
        
    else:
        print("Invalid Input, please run the program again.")
        break