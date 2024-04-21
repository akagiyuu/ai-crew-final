from student_manager import StudentManager
from student import Student
from data_structure.vec_dequeue import VecDequeue
from ui.menu import menu
from ui.required_input import required_input

MAIN_TITLE = "Student management system"
MAIN_MENU_OPTIONS = VecDequeue[str]()
MAIN_MENU_OPTIONS.push_back("Add student")
MAIN_MENU_OPTIONS.push_back("Delete student")
MAIN_MENU_OPTIONS.push_back("Update student")
MAIN_MENU_OPTIONS.push_back("Get student")
MAIN_MENU_OPTIONS.push_back("Get all students")
MAIN_MENU_OPTIONS.push_back("Save")
MAIN_MENU_OPTIONS.push_back("Quit")

manager = StudentManager()

while True:
    choosen_option = menu(MAIN_TITLE, MAIN_MENU_OPTIONS)
    print()
    match choosen_option:
        case 0:
            id = required_input("Enter id: ")
            full_name = required_input("Enter full name: ")
            date_of_birth = required_input("Enter date of birth: ")
            hometown = required_input("Enter hometown: ")
            faculty = required_input("Enter faculty: ")
            major = required_input("Enter major: ")
            student_class = required_input("Enter class: ")
            student = Student(
                id, full_name, date_of_birth, hometown, faculty, major, student_class
            )
            try:
                manager.add(student)
            except RuntimeError as err:
                print("Error:", err)
        case 1:
            id = required_input("Enter id: ")
            try:
                manager.delete(id)
            except RuntimeError as err:
                print("Error:", err)
        case 2:
            id = required_input("Enter id: ")
            full_name = input("Enter full name: ") or None
            date_of_birth = input("Enter date of birth: ") or None
            hometown = input("Enter hometown: ") or None
            faculty = input("Enter faculty: ") or None
            major = input("Enter major: ") or None
            student_class = input("Enter class: ") or None
            try:
                manager.update(
                    id,
                    full_name,
                    date_of_birth,
                    hometown,
                    faculty,
                    major,
                    student_class,
                )
            except RuntimeError as err:
                print("Error:", err)
        case 3:
            id = required_input("Enter id: ")
            student = manager.get_student(id)
            if student is None:
                print("Student not found")
            else:
                print(student)
        case 4:
            print(manager.students)
        case 5:
            manager.save()
        case 6:
            manager.save()
            break
        case _:
            raise RuntimeError("Unknown error")
