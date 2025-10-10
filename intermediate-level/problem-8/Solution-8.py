# simple_cli.py

def main():
    # Take user input, like: add 5 7
    command = input("Enter command: ").split()

    if not command:
        print("No command given.")
        return

    action = command[0]

    if action == "add":
        if len(command) != 3:
            print("Usage: add <num1> <num2>")
        else:
            num1 = float(command[1])
            num2 = float(command[2])
            print(num1 + num2)

    elif action == "sub":
        if len(command) != 3:
            print("Usage: sub <num1> <num2>")
        else:
            num1 = float(command[1])
            num2 = float(command[2])
            print(num1 - num2)

    elif action == "mul":
        if len(command) != 3:
            print("Usage: mul <num1> <num2>")
        else:
            num1 = float(command[1])
            num2 = float(command[2])
            print(num1 * num2)

    elif action == "div":
        if len(command) != 3:
            print("Usage: div <num1> <num2>")
        else:
            num1 = float(command[1])
            num2 = float(command[2])
            if num2 == 0:
                print("Error: Division by zero!")
            else:
                print(num1 / num2)

    else:
        print(f"Unknown command: {action}")


if __name__ == "__main__":
    main()
