print("--- Lab 4.1: Student Management System ---")

# 1) เริ่มต้นด้วย list ว่างสำหรับเก็บชื่อนักศึกษา
student_names = []

# 2) เพิ่มนักศึกษา: รับชื่อจากผู้ใช้ 3 คน แล้ว append() เข้า list
print("\n[1] Add Students")
for i in range(3):
    name = input(f"Enter student name #{i + 1}: ")
    student_names.append(name)

print(f"Current list: {student_names}")

# 3) ค้นหานักศึกษา
print("\n[2] Find a Student")
search_name = input("Enter a name to search for: ")

if search_name in student_names:
    position = student_names.index(search_name)
    print(f"Found '{search_name}' at index {position}")
else:
    print(f"'{search_name}' not found in the list")

# 4) ลบนักศึกษา
print("\n[3] Remove a Student")
remove_name = input("Enter a name to remove: ")

if remove_name in student_names:
    student_names.remove(remove_name)
    print(f"'{remove_name}' has been removed")
else:
    print(f"'{remove_name}' not found, nothing removed")

print(f"Updated list: {student_names}")

# 5) เรียงลำดับ
print("\n[4] Sort Students")
student_names.sort()
print(f"Sorted list: {student_names}")

# 6) นับจำนวนนักศึกษา
print("\n[5] Count Students")
print(f"Total students: {len(student_names)}")