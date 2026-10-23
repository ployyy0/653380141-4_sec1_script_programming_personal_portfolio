print("===== Challenge =====")

student_names = []

while True:
    print("\n===== Student Management =====")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Find Student")
    print("4. Sort Students")
    print("5. Show Students")
    print("6. Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Enter student name: ")
        student_names.append(name)
        print("Added successfully.")

    elif choice == "2":
        name = input("Enter student name to remove: ")
        if name in student_names:
            student_names.remove(name)
            print("Removed successfully.")
        else:
            print("Student not found.")

    elif choice == "3":
        name = input("Enter student name to search: ")
        if name in student_names:
            print(f"Found at index {student_names.index(name)}")
        else:
            print("Student not found.")

    elif choice == "4":
        student_names.sort()
        print("Sorted successfully.")
        print(student_names)

    elif choice == "5":
        print(student_names)
        print("Total:", len(student_names))

    elif choice == "6":
        print("Exit Program")
        break

    else:
        print("Invalid choice")