class Student:
    def __init__(
        self,
        id: str,
        full_name: str,
        date_of_birth: str,
        hometown: str,
        faculty: str,
        major: str,
        student_class: str
    ) -> None:
        self.id = id
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.hometown = hometown
        self.faculty = faculty
        self.major = major
        self.student_class = student_class
        pass
    def __str__(self) -> str:
        return (
            "Student: [\n"
            f"    id: {self.id} \n"
            f"    full_name: {self.full_name}\n"
            f"    date_of_birth: {self.date_of_birth}\n"
            f"    hometown: {self.hometown}\n"
            f"    faculty: {self.faculty}\n"
            f"    major: {self.major}\n"
            f"    class: {self.student_class}\n"
            "]"
        )
