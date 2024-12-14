Author: Kirkeisha McNish

Date Created: 12.12.2024

Course: ITT103 

GitHub Public URL to Code: https://github.com/Kittania/Registration_system.git 

Program Purpose: The program is a Student Registration System designed to perform various functions such as registering a student, adding a course (course ID, name and fee), enrolling a student (adding each course, course fee and balance), taking payment (ensuring they pay at least 40% of their balance) and viewing various data such as all students enrolled in a particular course and all courses added to the system.

How to Run the Program: To run the program, you will need a python interpreter and basic understating of how to run python scripts. Once you have access to the saved file, open a command prompt run the script. Once the script runs the program will come up with a menu with numbered options. Once you enter corresponding number the program will perform the different actions  

Assumptions
1.	Each student is identified uniquely by their student_id.
2.	Each course is identified by its course_id.
3.	Duplicates are not allowed.
4.	Payments must be at least 40% of the outstanding balance and the student balances can be zero    or greater, and overpayments can also be made.
5.	The user must manually select an option and input data correctly (e.g., no direct validations for non-numeric course fees).
6.	Data is stored only in memory and will not be saved once you exit the program.

Limitations
1.	No authentication option 
2.	The program does not save data to a file or database. All data is lost when the program ends.
3.	Limited error handling exists for invalid inputs (e.g., non-numeric IDs or fees).
4.	The requirement for a minimum payment of 40% cannot be changed. 

