pass_count = 0

for student_number in range(1, 5):
    score = float(input(f"Enter score for student {student_number}: "))

    if score >= 50:
        pass_count += 1

print(f"Number of passes: {pass_count}")
