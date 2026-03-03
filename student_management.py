# Student Management System

students = []

def add_student():
    
    while True:
        student_id = input("Enter Student ID (only letters and numbers): ")
        if student_id.isalnum():
            break
        else:
            print("Invalid ID! Only letters and numbers are allowed. Please try again.\n")
    
    while True:
        name = input("Enter Student Name: ")
        cleaned_name = " ".join(name.split())
        
        if cleaned_name.replace(" ", "").isalpha() and cleaned_name != "":
            name = cleaned_name
            break
        else:
            print("Invalid Name! Only letters and spaces are allowed. Please try again.\n")
    
    while True:
        marks = input("Enter Marks : ")
        
        if marks.isdigit() and 0 <= int(marks) <= 1000:
            marks = int(marks)
            break
        else:
            print("Invalid Marks! Please enter a number between 0 and 1000.\n")
    
    student = {
        "id": student_id,
        "name": name,
        "marks": marks
    }
    
    students.append(student)
    print("Student Added Successfully!\n")


def view_students():
    if not students:
        print("No students found.\n")
        return
    
    print("\nStudent List:")
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, Marks: {student['marks']}")
    print()


def search_student():
    if not students:
        print("No students found.\n")
        return
    
    search_term = input("Enter Student ID or Name to search: ")
    
    found = False
    for student in students:
        if student["id"] == search_term or student["name"].lower() == search_term.lower():
            print(f"Found -> ID: {student['id']}, Name: {student['name']}, Marks: {student['marks']}")
            found = True
    
    if not found:
        print("No matching record found. Please try again with correct ID or Name.\n")


def calculate_average():
    if not students:
        print("No students available.\n")
        return
    
    total = sum(student["marks"] for student in students)
    average = total / len(students)
    print(f"Average Marks: {average:.2f}\n")


def find_topper():
    if not students:
        print("No students available.\n")
        return
    
    highest_marks = max(student["marks"] for student in students)
    toppers = [student for student in students if student["marks"] == highest_marks]
    
    print("Topper(s):")
    for topper in toppers:
        print(f"{topper['name']} (Marks: {topper['marks']})")
    print()


def main():
    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Display Average Marks")
        print("5. Identify Topper")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            calculate_average()
        elif choice == "5":
            find_topper()
        elif choice == "6":
            print("Exiting Program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")


if __name__ == "__main__":
    main()