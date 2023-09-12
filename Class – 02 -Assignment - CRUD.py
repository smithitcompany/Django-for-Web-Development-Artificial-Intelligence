# Student Information Database
student_information = [
    {"Name": "Md. Hasan Ahmed", "Roll": "202101", "Group": "Science", "Year": "2023"},
    {"Name": "Farhana Khan", "Roll": "202465102", "Group": "Commerce", "Year": "2023"},
    {"Name": "Shamsul Haque", "Roll": "202146603", "Group": "Science", "Year": "2023"},
    {"Name": "Rafiqul Islam", "Roll": "202194504", "Group": "Arts", "Year": "2023"},
    {"Name": "Amina Begum", "Roll": "20210485", "Group": "Commerce", "Year": "2023"},
    {"Name": "Rezaul Karim", "Roll": "20210646", "Group": "Science", "Year": "2023"},
    {"Name": "Anika Rahman", "Roll": "20254107", "Group": "Commerce", "Year": "2023"},
    {"Name": "Sarwar Khan", "Roll": "2022108", "Group": "Arts", "Year": "2023"},
    {"Name": "Smith", "Roll": "159159", "Group": "Arts", "Year": "2026"}
]

# Main menu loop
while True:
    print("1. View Student Information")
    print("2. Add New Student")
    print("3. Update Student Information")
    print("4. Delete Student Record")
    print("5. Quit")
    admin_choice = input("Please select an action (1/2/3/4/5): ")

    if admin_choice == "5":
        print("You have quit the program.")
        break
    # Student Information
    elif admin_choice == "1":
        print("Student Information:")
        print("")  # This print for make the output more amazing
        for student in student_information:
            print("Name:", student["Name"])
            print("Roll:", student["Roll"])
            print("Group:", student["Group"])
            print("Year:", student["Year"])
            print("")
    # Add new student
    elif admin_choice == "2":
        try:
            add_new_student = input("Enter New Student Name: ")
            add_new_student_roll = input("Enter New Student's Roll: ")
            add_new_student_roll = int(add_new_student_roll)
            add_group = input("Enter New Student's Group: ")
            add_year = input("Enter New Student's Year: ")
            add_year = int(add_year)

            if 1920 <= add_year <= 2030:  # This is for if any one input wrong year Example:1512,526541. so I did
                # make a change that they can add a valid year
                student_information.append({
                    "Name": add_new_student,
                    "Roll": add_new_student_roll,
                    "Group": add_group,
                    "Year": add_year
                })
                print("New student added successfully!")
            else:
                print("Please enter a valid year within the range 1920-2030.")
        except ValueError:
            print("Please enter a valid number for the menu option.")
    # Update student information
    elif admin_choice == "3":
        try:
            print("1. Update Student Name")
            print("2. Update Student Roll")
            print("3. Update Student Group")
            print("4. Update Student Year")

            update_choice = input("Please select an action (1/2/3/4): ")

            if update_choice == "1":
                name_to_update = input("Enter Student Name To Update: ")
                new_name = input("Enter the Correct Name: ")
                for student in student_information:
                    if student["Name"] == name_to_update:
                        student["Name"] = new_name
                        print(f"{name_to_update} has been updated to {new_name}")
                        break
                else:
                    print("No Matching Student Found")
            elif update_choice == "2":
                full_name = input("Enter Student Full Name To Update Roll: ")
                new_roll = input("Enter the Correct Roll: ")
                for student in student_information:
                    if student["Name"] == full_name:
                        student["Roll"] = new_roll
                        print(f"{full_name} has been updated to {new_roll}")
                        break
                else:
                    print("No Matching Student Found")
            elif update_choice == "3":
                full_name = input("Enter Student Full Name To Update Group: ")
                try:
                    # roll_to_update = int(full_name)
                    new_group = input("Enter the Correct Group: ")
                    new_group = str(new_group)
                    for student in student_information:
                        if student["Name"] == full_name:
                            student["Group"] = new_group
                            print(f"{full_name}'s group has been updated to {new_group}")
                            break
                    else:
                        print("No Matching Student Found")
                except ValueError:
                    print("Please enter a valid number for the roll")
            elif update_choice == "4":
                full_name = input("Enter Student Full Name To Update Year: ")
                try:
                    new_year = input("Enter the Correct Year: ")
                    new_year = int(new_year)
                    if 1920 <= new_year <= 2030:
                        for student in student_information:
                            if student["Name"] == full_name:
                                student["Year"] = new_year
                                print(f"{full_name}'s year has been updated to {new_year}")
                                break
                        else:
                            print("No Matching Student Found")
                    else:
                        print("Please enter a valid year within the range 1920-2030.")
                except ValueError:
                    print("Please enter a valid number for the roll")
        except ValueError:
            print("Please enter a valid number for the menu option.")
# delete student recorde
    elif admin_choice == "4":
        delete_student_recorde = input("Enter Student Name To Delete Recorde: ")
        found = False  # A flag to check if the student is found and deleted
        # Iterate over the student information list
        for student in student_information:
            if student["Name"] == delete_student_recorde:
                student_information.remove(student)  # Remove the matching student record
                found = True  # Set the flag to True indication the student was found and deleted
                print(f"{delete_student_recorde}'s recorde has been deleted.")
                break  # No need to continue searching

        if not found:
            print("No Matching Student Found")
