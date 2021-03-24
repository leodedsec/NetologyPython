class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = [] #Полностью решенные и проверенные учителем курсы
        self.courses_in_progress = ["GIT"] #Студент записан на эти курсы
        self.grades = {} #Оценки
    def gradeLector(self, lector):
        for i in self.courses_in_progress:
            if i in Lectors.courses_attached:
                listGrades=[int(i) for i in range(11)] #оценки по 10-бальной шкале
                getGrade=""
                while getGrade not in listGrades:
                    getGrade=int(input("Оценка:"))
                Lectors.lectorGrades.append(getGrade)
            else:
                print("Error!")




class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        #Список курсов, которые может проверить учитель
        courses_attached=["GIT"]
        self.courses_attached = courses_attached


class Reviewers(Mentor):
    def rate_hw(self, student, course, grade):
        #Если экземпляр класса относится к классу Student и если курс имеется у учителя/студента, то:
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"


class Lectors(Mentor):
    lectorGrades=[]



lector1=Lectors("Oleg","Nazarov")

pupil1=Student("Azat","Messi","M")
pupil1.gradeLector(lector1)

print(lector1.courses_attached)