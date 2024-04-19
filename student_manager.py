from data_structure.vec_dequeue import VecDequeue
from student import Student


class StudentManager:
    def __init__(self) -> None:
        self.students = VecDequeue[Student]()

    def __contains__(self, id: str) -> bool:
        return self.get_student_index(id) is not None

    def get_student_index(self, id: str) -> int | None:
        index = 0
        for student in self.students:
            if student.id == id:
                return index
            index += 1
        return None

    def get_student(self, id: str) -> Student | None:
        for student in self.students:
            if student.id == id:
                return student
        return None

    def add(self, student: Student) -> None:
        if student.id in self:
            raise RuntimeError("Attempt to add existing student")

        self.students.push_back(student)

    def delete(self, id: str) -> None:
        student_index = self.get_student_index(id)
        if student_index is None:
            raise RuntimeError("Attempt to delete non-existing student")

        self.students.remove(student_index)

    def update(
        self,
        id: str,
        full_name: str | None = None,
        date_of_birth: str | None = None,
        hometown: str | None = None,
        faculty: str | None = None,
        major: str | None = None,
        student_class: str | None = None,
    ):
        student = self.get_student(id)
        if student is None:
            raise RuntimeError("Attempt to update non-existing student")

        if full_name is not None:
            student.full_name = full_name
        if date_of_birth is not None:
            student.date_of_birth = date_of_birth
        if hometown is not None:
            student.hometown = hometown
        if faculty is not None:
            student.faculty = faculty
        if major is not None:
            student.major = major
        if student_class is not None:
            student.student_class = student_class
