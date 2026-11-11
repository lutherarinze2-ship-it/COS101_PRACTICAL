number = int(input("Enter a whole number: "))
print()
print(f"Multiplication Table For {number}")
print("===============================")

for multiplier in range (1, 13):
    result = number * multiplier
    print(f"{number} x {multiplier} = {result}")
