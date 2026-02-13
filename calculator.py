def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

print("=== Simple Calculator v2 ===")

while True:
    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power (a^b)")
    print("6. Exit")
    choice = input("Enter choice (1-6): ")

    if choice == "6":
        print("Goodbye 👋")
        break
    elif choice == '5':
    print("Result:", num1 ** num2)

    if choice not in ["1", "2", "3", "4","5"]:
        print("Invalid choice. Try again.")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        print("Result:", add(num1, num2))
    elif choice == "2":
        print("Result:", sub(num1, num2))
    elif choice == "3":
        print("Result:", mul(num1, num2))
    elif choice == "4":
        print("Result:", div(num1, num2))

