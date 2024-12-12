#class for each student
class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = []
        self.balance = 0

#class for each course
class Course:
    def __init__(self, course_id, name, fee):
        self.course_id = course_id
        self.name = name
        self.fee = fee

#class for the system itself as well as course enrollment and payments
class RegistrationSystem:
    def __init__(self):
        self.students = {}
        self.courses = {}

# registering a student
    def register_student(self):
        student_id = input("Enter ID number: ")
        if student_id in self.students:
            print("Student already registered.")
        else:
            name = input("Enter name: ")
            self.students[student_id] = Student(student_id, name)
            print(f"Student {name} registered successfully.")

# adding a course
    def add_course(self):
        course_id = input("Enter course ID: ")
        if course_id in self.courses:
            print("Course ID already added.")
        else:
            name = input("Enter course name: ")
            fee = float(input("Enter course amount: "))
            self.courses[course_id] = Course(course_id, name, fee)
            print(f"Course {name} was successfully added.")

#enrolling a student to accept course ID and student name
    def enroll_student(self):
        student_id = input("Enter student ID: ")
        if student_id not in self.students:
            print("No student with that ID was found.")
            return
        course_id = input("Enter course ID: ")
        if course_id not in self.courses:
            print("Course not found. Please add course to proceed. ")
            return
        student = self.students[student_id]
        course = self.courses[course_id]

    #checking to see if the student is already enrolled
        if course_id in [c.course_id for c in student.courses]:
            print(f"{student.name} is already enrolled in {course.name}.")
        else:

    #enroll the student and display the student balance based on the course added
            student.courses.append(course)
            student.balance += course.fee
            print(f"{student.name} has been enrolled in {course.name}.")
            print(f" Balance, ${student.balance:.2f}")

    #take payment for the courses the students are enrolled in
    def accept_payment(self):
        student_id = input("Enter student ID: ")
        if student_id not in self.students:
            print("Student not found. Please register student before attempting enrollment.")
            return

    #checking if the student have a balance
        student = self.students[student_id]
        if student.balance == 0:
            print("No outstanding balance.")
            return
        print(f"Current balance: ${student.balance:.2f}")
        amount = float(input("Enter payment amount: "))

    #based on balance shown, ensure payment is at least 40% of the total
        if amount < 0.4 * student.balance:
            print("Payment should be at least 40% of the outstanding balance.")
        else:
            student.balance -= amount
            print(f"Payment successful. New balance: ${student.balance:.2f}")

    #showing all students who are registered
    def view_students(self):
        if not self.students:
            print("No students registered.")
            return
        for student_id, student in self.students.items():
            print(f"Student ID: {student_id}, Name: {student.name}, "
                  f"Enrolled Courses: {[course.name for course in student.courses]}, "
                  f"Balance: ${student.balance:.2f}")

    #this shows all courses that were added to the system
    def view_courses(self):
        if not self.courses:
            print("No available courses.")
            return
        for course_id, course in self.courses.items():
            print(f"Course ID: {course.course_id}, Name: {course.name}, Fee: ${course.fee:.2f}")

    #shows all students who are registered in each listed course
    def show_students_in_course(self):
        course_id = input("Enter course ID: ")
        if course_id not in self.courses:
            print("Course not found.")
            return
        course = self.courses[course_id]
        students_in_course = [
            f"ID: {student.student_id}, Name: {student.name}"
            for student in self.students.values()
            if any(c.course_id == course_id for c in student.courses)
        ]
        if students_in_course:
            print(f"Students enrolled in {course.name}:")
            for student_info in students_in_course:
                print(student_info)
        else:
            print(f"No students enrolled in {course.name}.")

#main menu to perform all functions of the program
    def menu(self):
        while True:
            print("\n Menu Options")
            print("1. Register Student")
            print("2. Add Course")
            print("3. Enroll Student in Course")
            print("4. Accept Payment")
            print("5. View All Students")
            print("6. View All Courses")
            print("7.Show all students registered in course")
            print("8. Exit")
            try:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    self.register_student()
                elif choice == 2:
                    self.add_course()
                elif choice == 3:
                    self.enroll_student()
                elif choice == 4:
                    self.accept_payment()
                elif choice == 5:
                    self.view_students()
                elif choice == 6:
                    self.view_courses()
                elif choice == 7:
                    self.show_students_in_course()
                elif choice == 8:
                    print("Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                    print("Please enter a number.")



if __name__ == "__main__":
    system = RegistrationSystem()
    system.menu()
