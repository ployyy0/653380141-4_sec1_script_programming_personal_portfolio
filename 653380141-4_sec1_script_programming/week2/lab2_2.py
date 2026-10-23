
# รับอายุจากผู้ใช้
age = int(input("Enter your age: "))

# แนะนำเรตภาพยนตร์ตามอายุ
if age < 5:
    print("You're too young for movies! Enjoy cartoons.")
elif age <= 12:
    print("Recommended: G-rated or PG-rated movies.")
elif age <= 17:
    print("Recommended: PG-13 or R-rated (with parental guidance).")
else:
    print("Recommended: Any movie rating.")

    # Challenge
    action = input("Do you like action movies? (yes/no): ").lower()

    if action == "yes":
        print("You might enjoy the latest action blockbuster!")
    elif action == "no":
        print("Maybe you would enjoy another movie genre.")
    else:
        print("Error: Please enter only 'yes' or 'no'.")