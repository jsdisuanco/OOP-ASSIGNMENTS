while True:

    print("\nChoose operation:")
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")
    print("5 - Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == "5":
        print("Exiting calculator. Goodbye!")
        break

    if choice in ["1", "2", "3", "4"]:

        # Keep asking until first number is valid
        while True:
            try:
                num1 = float(input("Enter first number: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        # Keep asking until second number is valid
        while True:
            try:
                num2 = float(input("Enter second number: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        # Perform calculation
        if choice == "1":
            print(f"{num1} + {num2} = {num1 + num2}")

        elif choice == "2":
            print(f"{num1} - {num2} = {num1 - num2}")

        elif choice == "3":
            print(f"{num1} * {num2} = {num1 * num2}")

        elif choice == "4":
            while num2 == 0:
                print("Cannot divide by zero.")
                try:
                    num2 = float(input("Enter second number again: "))
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            print(f"{num1} / {num2} = {num1 / num2}")

    else:
        print("Invalid choice. Please select 1-5.")