n = int(input("Enter a + number: "))

if n < 1:
    print("Invalid input.")
else:
    total = 0

    for number in range (1, n + 1):
        total += number
        
    print(f"The sum from 1 to {n} is {total}.")
