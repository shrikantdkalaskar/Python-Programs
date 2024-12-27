while True: 
    x = z
    x = float(input("Enter the First Number: "))
    y = float(input("Enter the Second Number: "))
    print("Press 1 for Addition \nPress 2 for Subtraction \nPress 3 for Multiplication \nPress 4 for Division")
    c = int(input("Choose the operation: "))

    match c:
        case 1:
            z = x + y
            print("Result:", z)
        case 2:
            z = x - y
            print("Result:", z)
        case 3:
            z = x * y
            print("Result:", z)
        case 4:
            if y == 0:
                print("Error: Division by zero is not allowed.")
            else:
                z = x / y
                print("Result:", z)
        case _:
            print("Please choose a valid operation.")

    choice = input("Do you want to perform another operation? (yes to continue, no to exit): ")
    if choice != "yes": 
        print("Exiting the program. Goodbye!")
        break