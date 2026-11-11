while True:
    num = int(input("Enter a number greater than 1: "))

    while num <= 1:
        print("Please enter a number greater than 1!")
        num = int(input("Enter another number: "))

    for i in range(1, 13):
        print(f"{num} x {i} = {num * i}")

    choice = input("\nPress X to exit or Enter to continue: ")

    if choice.upper() == "X":
        print("Program terminated.")
        break
