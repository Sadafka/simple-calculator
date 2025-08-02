# Simple Calculator Program - 10 Mordad

print("====== Simple Calculator ======")
print("Select operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

while True:
    # Get user choice
    choice = input("Enter choice (1/2/3/4): ")

    # Check if choice is valid
    if choice in ('1', '2', '3', '4'):
        # Get two numbers
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"Result: {num1} + {num2} = {num1 + num2}")

        elif choice == '2':
            print(f"Result: {num1} - {num2} = {num1 - num2}")

        elif choice == '3':
            print(f"Result: {num1} * {num2} = {num1 * num2}")

        elif choice == '4':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                print(f"Result: {num1} / {num2} = {num1 / num2}")

        # Ask if user wants another calculation
        next_calc = input("Do you want to calculate again? (yes/no): ")
        if next_calc.lower() != 'yes':
            print("Calculator closed. Goodbye!")
            break

    else:
        print("Invalid input. Please enter 1, 2, 3, or 4.")