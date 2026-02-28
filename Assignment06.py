# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   SKennedy,02/27/2026,Created Script
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Constants
# FILE_NAME: str = "Enrollments.csv"


# Define the Data Variables and constants
# student_first_name: str = ''  # Holds the first name of a student entered by the user.
# student_last_name: str = ''  # Holds the last name of a student entered by the user.
# course_name: str = ''  # Holds the name of a course entered by the user.
# student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
menu_choice: str = ''  # Hold the choice made by the user.
#file = None  # Holds a reference to an opened file.

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file

class FileProcessor:
    """
    A collection of processing layer functions that work with json files

    ChangeLog: (Who, When, What)
    SKennedy, 2/27/2026, Created Class
    """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ Reads data from a JSON file and loads it into a list.
        """
        file = None
        try:
            file = open(file_name, "r")
            # Clear existing list and load new data
            student_data.clear()
            student_data.extend(json.load(file))
        except FileNotFoundError as e:
            # Create the file if it doesn't exist to avoid initial crash
            IO.output_error_message("The file was not found. Starting with empty list.")
        except Exception as e:
            IO.output_error_message("Error: There was a problem with reading the file.", e)
    # print("Please check that the file exists and that it is in a json format.")
    # print("-- Technical Error Message -- ")
    # print(e.__doc__)
    # print(e.__str__())
        finally:
    # Check if a file object exists and is still open
            if file is not None and file.closed == False:
                file.close()
    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """
        Write data from a list of dictionaries to a JSON file.
        """
        file=None
        success = False
        try:
            file=open(file_name, "w")
            json.dump(student_data, file, indent=2)
            success = True
        except Exception as e:
            IO.output_error_messages("Error: There was a problem writing to the file.",e)
        finally:
            if file is not None and not file.closed:
                file.close()
        if success:
            print("\nData successfully saved to file.")

# Present and Process the data
class IO:
    """
    A collection of functions to handle input and output operations.
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception=None):
        """ Display a custom error message to the user.
        """
        print(f"\n{message}")
        if error is not None:
            print("--Technical Error Message --")
            print(error.__doc__)
            print(error.__str__())

#while (True):
    @staticmethod
    def output_menu(menu: str):
        """
        Displays the menu of choices to the user.
        """
        print(menu)

    @staticmethod
    def input_menu_choice():
        """
        Prompts the user for a menu choice.
        """
        choice = input("What would you like to do: ")
        return choice

    # Present the menu of choices
    # print(MENU)
    # menu_choice = input("What would you like to do: ")

    # Input user data
    @staticmethod
    def output_student_courses(student_data: list):
        """
        Displays the list of current student enrollments.
        """
        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} {student["LastName"]} '
                    f'is enrolled in {student["CourseName"]}')
        print("-" * 50)

    # if menu_choice == "1":  # This will not work if it is an integer!
    @staticmethod
    def input_student_data(student_data: list):
        """
        Prompts user for student data and appends it to the list.
        """
        try:
            first_name = input("Enter the student's first name: ")
            if not first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")

            last_name = input("Enter the student's last name: ")
            if not last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")

            course = input("Please enter the name of the course: ")

            new_student = {
                "FirstName": first_name,
                "LastName": last_name,
                "CourseName": course
                }
            student_data.append(new_student)
            print(f"\nYou have registered {first_name} {last_name} for {course}.")

        except ValueError as e:
                IO.output_error_messages("Data Entry Error:", e)
            # print(e)  # Prints the custom message
            # print("-- Technical Error Message -- ")
            # print(e.__doc__)
            # print(e.__str__())
        except Exception as e:
            IO.output_error_messages("An unexpected error occured during input.", e)
            # print("Error: There was a problem with your entered data.")
            # print("-- Technical Error Message -- ")
            # print(e.__doc__)
            # print(e.__str__())

    # Present the current data
FileProcessor.read_data_from_file(FILE_NAME, students)

while True:
    
    IO.output_menu(MENU)
    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":
        IO.input_student_data(students)

    elif menu_choice == "2":
        IO.output_student_courses(students)

        # Process the data to create and display a custom message
        # print("-" * 50)
        # for student in students:
        #     print(f'Student {student["FirstName"]} '
        #           f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        # print("-" * 50)
        # continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(FILE_NAME, students)
        IO.output_student_courses(students)

        # try:
        #     file = open(FILE_NAME, "w")
        #     json.dump(students, file, indent=2)
        #     print("The following data was saved to file!")
        #     for student in students:
        #         print(f'Student {student["FirstName"]} '
        #               f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        # except Exception as e:
        #     print("Error: There was a problem with writing to the file.")
        #     print("Please check that the file is not open by another program.")
        #     print("-- Technical Error Message -- ")
        #     print(e.__doc__)
        #     print(e.__str__())
        # finally:
        #     # Check if a file object exists and is still open
        #     if file is not None and file.closed == False:
        #         file.close()
        # continue

    # Stop the loop
    elif menu_choice == "4":
        print("Exiting Program...")
        break  # out of the loop
    else:
        print("Please enter a valid choice (1, 2, 3, or 4).")

print("Program Ended")
