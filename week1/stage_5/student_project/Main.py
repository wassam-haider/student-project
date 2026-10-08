from Validate import validate_name, validate_marks
from Calculate import calculate_grade
from Student import Student 
from Report import display_report

def main():
    name = input("Enter student name: ")
    if not validate_name(name):
        print("Invalid name")
        return
    marks = int(input("Enter marks: "))
    if not validate_marks(marks):
        print("Invalid marks")
        return
    grade = calculate_grade(marks)
    student = Student(name, marks, grade)
    # below not in given code just for checking
    display_report(student)

if __name__ == "__main__":
    main()