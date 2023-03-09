GradeSet = set([_ for _ in range(11)])


def average(dic_t):
    """Count medium value of dict values"""
    s = 0
    h = 0
    for key in dic_t:
        s += sum(dic_t[key])
        h += len(dic_t[key])
    ave = round(s/h, 1)
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
            return 'Ошибка'

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
            return 'Ошибка'

    def __str__(self):
        res = f"""Имя: {self.name}
Фамилия: {self.surname}"""
        return res


if __name__ == '__main__':
    best_student = Student('Ruoy', 'Eman', 'your_gender')
    best_student.courses_in_progress += ['Python']

    cool_mentor = Reviewer('Some', 'Buddy')
    cool_mentor.courses_attached += ['Python']

    cool_mentor.rate_hw(best_student, 'Python', 10)
    cool_mentor.rate_hw(best_student, 'Python', 7)
    cool_mentor.rate_hw(best_student, 'Python', 9)
    print(best_student)
    # print(best_student.grades)
