from student_app.utils.validation import validate_name, validate_marks
from student_app.services.calculator import calculate_grade
from student_app.models.student import Student 
from student_app.reports.student_report import display_report

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