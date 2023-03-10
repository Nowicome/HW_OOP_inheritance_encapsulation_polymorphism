GradeSet = set([_ for _ in range(11)])
student_list = []
reviewer_list = []
lecturer_list = []


def average(dic_t):
    """Count medium value of dict values"""
    s = 0
    h = 0
    for key in dic_t:
        s += sum(dic_t[key])
        h += len(dic_t[key])
    ave = round(s/h, 1)
    return ave


def ave_stu(stu_list, course):
    ave = 0
    for student in stu_list:
        if course in student.courses_in_progress or course in student.finished_courses:
            ave += average(student.grades)
    return ave


def ave_lec(lec_list, course):
    ave = 0
    for lecturer in lec_list:
        if course in lecturer.courses_attached:
            ave += average(lecturer.grades)
    return ave


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_le(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and grade in GradeSet \
                and (course in self.courses_in_progress or course in self.finished_courses):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"

    def __str__(self):
        res = f"""Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {average(self.grades)}
Курсы в процессе изучения: {", ".join(self.courses_in_progress)}
Завершённые курсы: {", ".join(self.finished_courses)}"""
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            return print("Not a Student")
        return average(self.grades) < average(other.grades)

    def __le__(self, other):
        if not isinstance(other, Student):
            return print("Not a Student")
        return average(self.grades) <= average(other.grades)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        res = f"""Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {average(self.grades)}"""
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return print("Not a Lecturer")
        return average(self.grades) < average(other.grades)

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            return print("Not a Lecturer")
        return average(self.grades) <= average(other.grades)


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and grade in GradeSet \
                and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"

    def __str__(self):
        res = f"""Имя: {self.name}
Фамилия: {self.surname}"""
        return res


if __name__ == "__main__":
    student_one = Student("Maria", "Hines", "female")
    student_list.append(student_one)
    student_one.courses_in_progress += ["Python"]
    student_two = Student("Eric", "Williams", "male")
    student_list.append(student_two)
    student_two.courses_in_progress += ["Java"]

    reviewer_one = Reviewer("Viola", "Watson")
    reviewer_list.append(reviewer_one)
    reviewer_one.courses_attached += ["Python"]
    reviewer_two = Reviewer("Timothy", "James")
    reviewer_list.append(reviewer_two)
    reviewer_two.courses_attached += ["Java"]

    lecturer_one = Lecturer("Thomas", "Garcia")
    lecturer_list.append(lecturer_one)
    lecturer_one.courses_attached += ["Python"]
    lecturer_two = Lecturer("Deborah", "Castillo")
    lecturer_list.append(lecturer_two)
    lecturer_two.courses_attached += ["Java"]

    reviewer_one.rate_hw(student_one, "Python", 10)
    reviewer_one.rate_hw(student_one, "Python", 7)
    reviewer_one.rate_hw(student_one, "Python", 9)

    reviewer_two.rate_hw(student_two, "Java", 5)
    reviewer_two.rate_hw(student_two, "Java", 7)
    reviewer_two.rate_hw(student_two, "Java", 6)

    student_one.rate_le(lecturer_one, "Python", 9)
    student_one.rate_le(lecturer_one, "Python", 10)
    student_one.rate_le(lecturer_one, "Python", 6)

    student_two.rate_le(lecturer_two, "Java", 5)
    student_two.rate_le(lecturer_two, "Java", 10)
    student_two.rate_le(lecturer_two, "Java", 3)

    print("Информация о студентах:")
    for i in range(len(student_list)):
        print(f"Студент №{i+1}")
        print(student_list[i])
        print()
    print("Информация о проверяющих:")
    for i in range(len(reviewer_list)):
        print(f"Проверяющий №{i + 1}")
        print(reviewer_list[i])
        print()
    print("Информация о лекторах:")
    for i in range(len(lecturer_list)):
        print(f"Лектор №{i + 1}")
        print(lecturer_list[i])
        print()

    print(student_one > student_two)
    print(lecturer_one >= lecturer_two)

    print("Средняя оценка по всем студентам курса Python")
    print(ave_stu(student_list, "Python"))

    print("Средняя оценка по всем лекторам курса Java")
    print(ave_lec(lecturer_list, "Java"))
