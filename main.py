from calculator import operations

def main():
    while True:
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            operation = input("Choose operation (+, -, *, /, %): ")

            if operation == '+':
                print("Result:", operations.add(num1, num2))
            elif operation == '-':
                print("Result:", operations.subtract(num1, num2))
            elif operation == '*':
                print("Result:", operations.multiply(num1, num2))
            elif operation == '/':
                print("Result:", operations.divide(num1, num2))
            elif operation == '%':
                print("Result:", operations.modulus(num1, num2))
            else:
                print("Invalid operation. Try again.")
                continue

            break  # Exit after one successful operation
        except ValueError:
            print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    main()
