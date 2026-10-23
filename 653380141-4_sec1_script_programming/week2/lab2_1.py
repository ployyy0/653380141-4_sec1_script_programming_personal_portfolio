
# lab2_1.py

# รับค่าจากผู้ใช้
number = int(input("Enter an integer: "))

# ตรวจสอบว่าเป็นจำนวนบวก ลบ หรือศูนย์
if number > 0:
    print("The number is Positive.")
elif number < 0:
    print("The number is Negative.")
else:
    print("The number is Zero.")

# ตรวจสอบว่าเป็นเลขคู่หรือเลขคี่
if number % 2 == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")

# Challenge: รวมเงื่อนไข
if number > 0 and number % 2 == 0:
    print("The number is positive and even.")
elif number > 0 and number % 2 != 0:
    print("The number is positive and odd.")
elif number < 0 and number % 2 == 0:
    print("The number is negative and even.")
elif number < 0 and number % 2 != 0:
    print("The number is negative and odd.")
else:
    print("The number is zero (an even number).")