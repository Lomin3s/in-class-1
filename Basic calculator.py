def main():


    try:
        operation = str(input("Enter the operation: "))

        number1 = float(input("Enter first operand: "))
        number2 = float(input("Enter second operand: "))

        if operation == "add":
            print("Result is ", number1 + number2)
        elif operation == "sub":
            print("Result is ", number1 - number2)
        elif operation == "mul":
            print("Result is ", number1 * number2)
        elif operation == "div":
            print("Result is ", number1 / number2)

    except:
        print("Invalid input")
        main()
main()
