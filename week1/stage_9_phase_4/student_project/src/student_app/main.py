# stage 1
# name = input("Enter student name: ")
# marks = int(input("Enter student marks: "))

# if marks >= 80:
#     grade = "A"
# elif marks >= 70:
#     grade = "B"
# elif marks >= 60:
#     grade = "C"
# elif marks >= 50:
#     grade = "D"
# else:
#     grade = "F"

# print()
# print("Student Report")
# print("----------------")
# print(f"Name: {name}")
# print(f"Marks: {marks}")
# print(f"Grade: {grade}")

# stage 2
# name = input("Enter student name: ")

# try:
#     marks = int(input("Enter student marks: "))
# except ValueError:
#     print("Error: Marks must be a number.")
#     exit()


# if marks < 0 or marks > 100:
#     print("Error: Marks must be between 0 and 100.")
#     exit()

# if marks >= 80:
#     grade = "A"
# elif marks >= 70:
#     grade = "B"
# elif marks >= 60:
#     grade = "C"
# elif marks >= 50:
#     grade = "D"
# else:
#     grade = "F"

# print()
# print("Student Report")
# print("----------------")
# print(f"Name: {name}")
# print(f"Marks: {marks}")
# print(f"Grade: {grade}")


# stage 3 and beyond
from logger import logger
from utils.validation import validate_name, validate_marks
from services.calculator import calculate_grade, is_pass

logger.info("Application started")

name = input("Enter student name: ")

if not validate_name(name):
    logger.warning("Empty student name entered")
    print("Error: Name cannot be empty.")
    exit()

try:
    marks = int(input("Enter student marks: "))
except ValueError:
    logger.error("Invalid marks entered: not a number")
    print("Error: Marks must be a number.")
    exit()


if not validate_marks(marks):
    logger.warning(f"Invalid marks entered: {marks}")
    print("Error: Marks must be between 0 and 100.")
    exit()

grade = calculate_grade(marks)
status = "Pass" if is_pass(marks) else "Fail"


logger.info(f"Grade calculated for {name}: {grade}")
            
print()
print("Student Report")
print("----------------")
print(f"Name: {name}")
print(f"Marks: {marks}")
print(f"Grade: {grade}")
print(f"Status: {status}")