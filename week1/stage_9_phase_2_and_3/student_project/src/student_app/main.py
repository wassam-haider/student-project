from config import APP_NAME
from config import DEBUG
from config import MAX_STUDENTS
import json

def student_loader():
    with open("../../data/student.json", "r") as file:
        student_data_from_json = json.load(file)
        return student_data_from_json

    
def main():
    print("Application Starting...")
    print()
    print(f"Application Name: {APP_NAME}")
    print(f"Debug Mode: {DEBUG}")
    print(f"Maximum Students: {MAX_STUDENTS}")
    std = student_loader()
    print("Student_json wali Information")
    print(f"ID: {std['id']}")
    print(f"Name: {std['name']}")
    print(f"Program: {std['program']}")
    print(f"Semester: {std['semester']}")
    print(f"Marks: {std['marks']}")

if __name__ == "__main__":
    main()