# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Reilly Thomer,11/19/2024,Script Edited
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
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
menu_choice: str  # Hold the choice made by the user.
students: list = []  # a table of student data`

#Classes and Functions
class IO:
    """
    A collection of functions that obtain user input,
    display data and strings, as well as contains an error handler
    ChangeLog: Reilly Thomer, 11.19.2024, Created Class
    """
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function prints an error message out
        ChangeLog: Reilly Thomer, 11.19.2024, Created Function
        :param message: string data that is to be displayed to the user
        :param error: exception that was raised to the error handler
        :return: back to the main script
        """
        print("-" * 50)
        print("Error: " + message)
        print("-- Technical Error Message -- ")
        print(error.__doc__)
        print(error.__str__())
        return

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu to the user
        ChangeLog: Reilly Thomer, 11.19.2024, Created Function
        :param menu: menu to be displayed to the user
        :return: back to the main script
        """
        print(menu)
        return

    @staticmethod
    def input_menu_choice():
        """ This function obtains the user input choice to the menu
        ChangeLog: Reilly Thomer, 11.19.2024, Created Function
        :return: the menu choice of the user
        """
        return input("What would you like to do: ")

    @staticmethod
    def input_student_data(student_data: list):
        """ This function obtains the student data through user prompts
         and appends them to the student data list
         ChangeLog: Reilly Thomer, 11.19.2024, Created Function
        :param student_data: list of student data that is added to
        :return: back to the main script
        """
        while(True):
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                IO.output_error_messages("The first name should not contain numbers.",Exception())
            else:
                break
        while(True):
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                IO.output_error_messages("The last name should not contain numbers.", Exception())
            else:
                break
        course_name = input("Please enter the name of the course: ")
        student = {"FirstName": student_first_name,
                        "LastName": student_last_name,
                        "CourseName": course_name}
        student_data.append(student)
        return

    @staticmethod
    def output_student_courses(student_data: list):
        """ This function prints all student data in the list for the user to view
        ChangeLog: Reilly Thomer, 11.19.2024, Created Function
        :param student_data: list of student data that is printed to the user
        :return: back to the main script
        """
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)
        return

class FileProcessor:
    """
    A collection of functions that perform file processing
    ChangeLog: Reilly Thomer, 11.19.2024, Created Class
    """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ This function reads all the data from the Json File
        ChangeLog: Reilly Thomer, 11.19.2024, Created Function
        :param file_name: string name for json file to be read
        :param student_data: list of student data that is to be writen to
        :return: back to the main script
        """
        try:
            file = open(file_name, "r")
            file_data = json.load(file)
            for item in file_data:
                student_data.append(item)
            return
        except Exception as e:
            IO.output_error_messages("There was a problem with reading the file.", e)
        finally:
            if file.closed == False:
                file.close()
            return

    @staticmethod
    def write_data_to_file(file_name:str, student_data:list):
        """ This function writes data to a json file
        ChangeLog: Reilly Thomer, 11.19.2024, Created Function
        :param file_name: string name of file json file to be written to
        :param student_data: list of student data to be written to json file
        :return: back to the main script
        """
        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
            print("The following data was saved to file!")
            for student in student_data:
                print(f'Student {student["FirstName"]} '
                      f'{student["LastName"]} is enrolled in {student["CourseName"]}')
            return
        except Exception as e:
            IO.output_error_messages("There was a problem with writing to the file.", e)
            if file.closed == False:
                file.close()
            return


#Beginning of the Main Body
FileProcessor.read_data_from_file(FILE_NAME,students)

while (True):
    #Outputs User Menu
    IO.output_menu(MENU)
    #Obtains User Menu Choice
    menu_choice = IO.input_menu_choice()
    # Process input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        IO.input_student_data(students)
    # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(students)
    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(FILE_NAME,students)
    # Stop the loop
    elif menu_choice == "4":
         break  # out of the loop
    #In case any other manu number is entered
    else:
        print("Please only choose option 1, 2, or 3")
print("Program Ended")