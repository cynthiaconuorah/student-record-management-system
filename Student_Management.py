# Course: IT3883/Section W01
# Student Name: Cynthia Onuorah
# Assignment Number: Lab4
# Due Date: 06/08/2025
# Purpose: The purpose is to input and save student records.


import os

# Global student dictionary
students = {}

# 1. Add student data
def add_student():
    first_name = input("Enter First Name: ").strip()
    last_name = input("Enter Last Name: ").strip()
    student_id = input("Enter Student ID: ").strip()
    gpa_input = input("Enter GPA: ").strip()
    
    try:
        gpa = float(gpa_input)
        students[student_id] = {
            "First Name": first_name,
            "Last Name": last_name,
            "GPA": gpa
        }
        print(f"Student {first_name} {last_name} added successfully.\n")
    except ValueError:
        print("Invalid GPA. Must be a number.\n")

# 2. Display all student records
def display_students():
    if not students:
        print("No student records found.\n")
        return

    print(f"{'Student ID':<15} {'Full Name':<25} {'GPA':<5} {'Status'}")
    print("-" * 60)
    for sid, data in students.items():
        full_name = f"{data['First Name']} {data['Last Name']}"
        gpa = data.get("GPA", "N/A")
        if gpa == "N/A":
            status = "N/A"
        else:
            if gpa >= 3.5:
                status = "Dean’s List"
            elif gpa < 2.0:
                status = "Probation"
            else:
                status = "Regular Standing"
        print(f"{sid:<15} {full_name:<25} {gpa:<5} {status}")
    print()

# 3. Remove GPA from a record
def remove_gpa():
    sid = input("Enter Student ID to remove GPA from: ").strip()
    if sid in students and "GPA" in students[sid]:
        del students[sid]["GPA"]
        print(f"GPA removed from student {sid}.\n")
    else:
        print("Student ID not found or GPA already removed.\n")

# 4. Save all records to students_dict.txt
def save_records():
    with open("students_dict.txt", "w") as file:
        for sid, data in students.items():
            first = data.get("First Name", "")
            last = data.get("Last Name", "")
            gpa = data.get("GPA", "N/A")
            file.write(f"{sid},{first},{last},{gpa}\n")
    print("All student records saved to students_dict.txt.\n")

# 5. Load from file and categorize again
def load_and_categorize():
    if not os.path.exists("students_dict.txt"):
        print("students_dict.txt not found.\n")
        return

    with open("students_dict.txt", "r") as infile, open("student_categories.txt", "w") as outfile:
        for line in infile:
            parts = line.strip().split(",")
            if len(parts) != 4:
                continue
            sid, first, last, gpa = parts
            try:
                gpa = float(gpa)
                if gpa >= 3.5:
                    status = "Dean’s List"
                elif gpa < 2.0:
                    status = "Probation"
                else:
                    status = "Regular Standing"
            except ValueError:
                gpa = "N/A"
                status = "N/A"
            outfile.write(f"{sid},{first} {last},{gpa},{status}\n")

    print("Student categories saved to student_categories.txt.\n")

# Menu Interface
def menu():
    while True:
        print("----- Student Management Menu -----")
        print("1. Add Student Record")
        print("2. Display All Students")
        print("3. Remove GPA from a Record")
        print("4. Save Records to File")
        print("5. Load and Categorize from File")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            remove_gpa()
        elif choice == "4":
            save_records()
        elif choice == "5":
            load_and_categorize()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.\n")

# Run the menu
if __name__ == "__main__":
    menu()
