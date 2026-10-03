# CYB434 - Lab 1 - Student Marks Calculator
# Name:Suhaib Ahmad Aljuhani
# University ID:4400240


def get_grade(mark):
    # Task 1: Replace this return with if / elif / else.
    # A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: 0-59.
    # Return the grade as text. Only valid marks reach this function.
   
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"


def calculate_average(total, count):
    # Task 3: Fix the arithmetic bug. For 80 and 81, expect 80.50.
    # count is positive when this function is called.
    return total / count


def main():
    # This input check is provided. Enter whole numbers only.
    number_of_marks = int(input("How many marks? "))
    while number_of_marks <= 0:
        print("Enter a positive number of marks.")
        number_of_marks = int(input("How many marks? "))

    total = 0
    count = 0
    while count < number_of_marks:
        mark = int(input("Enter mark: "))

        # Task 2: Replace False with a condition for an invalid mark.
        # Invalid means below 0 OR above 100. Do not count it.
        if mark < 0 or mark > 100:
            print("Invalid mark. Enter 0 to 100.")
        else:
            print("Grade:", get_grade(mark))
            # Task 3: Change this line to add the valid mark to total.
            total += mark
            count = count + 1

    average = calculate_average(total, count)
    print("Total:", total)
    print(f"Average: {average:.2f}")


# Run main only when this file is started directly, not when imported.
if __name__ == "__main__":
    main()

# Task 4: Answer after testing. Keep these as comments.
# Arithmetic fix: I changed // to / so the average includes decimal values.
# Count explanation: Invalid marks must not increase count because only valid marks should be counted.
# My test results: 80 and 81 gave total 161 and average 80.50. Invalid marks -1 and 101 were rejected.
