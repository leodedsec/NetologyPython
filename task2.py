class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = [] #Полностью решенные и проверенные учителем курсы
        self.courses_in_progress = [] #Курсы на проверку
        self.grades = {} #Оценки
    def __str__(self):
        return "Имя: "+self.name+"\n"+"Фамилия: "+self.surname+"\n"+\
        "Средняя оценка за домашние задания: "+str(sum(self.grades.values())/len(self.grades))+"\n"+\
        "Завершенные курсы: "+self.finished_courses
    #поставить оценку лектору
    def gradeLecturer(self,lector):
        rangeGrades=[int(i) for i in range(11)] #оценки 0-10
        getLecurer=list(map(str, input("Имя/Фамилия лектора:").split()))
        if getLecurer[0]==lector.name and getLecurer[1]==lector.surname:
            for i in self.courses_in_progress:
                if i in lector.courses_attached:
                    get_grade=None
                    while get_grade not in rangeGrades:
                        get_grade=int(input("Оценка лектору: "))
                    lector.grade_lecturer.append(get_grade)
                    break
            else:
                print("Наборы курсов у преподавателя/ученика разнятся!")
        else:
            print("Такого лектора не сущесвует в нашем вузе!")




class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = [] #Список доступных курсов на проверку

#Проверяющие ДЗ
class Reviewers(Mentor):
    def __str__(self):
        return "Имя: "+self.name+"\n"+"Фамилия: "+self.surname
    def rate_hw(self, student, course, grade):
        #Если экземпляр класса относится к классу Student
        #и если курс имеется у проверяющего and студента на проверке
        if isinstance(student, Student) and course in self.courses_attached\
        and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"

#Лекторы, которым студенты ставят оценки
class Lecturer(Mentor):
    def __str__(self):
        return "Имя: "+self.name+"\n"+"Фамилия: "+self.surname+"\n"+\
        "Средняя оценка за лекции: "+str(sum(self.grade_lecturer)/len(self.grade_lecturer))
    grade_lecturer=[]
    def addCourses(self):
        get_course=input("Введите название курса:")
        self.courses_attached.append(get_course)



lector1=Lecturer("Oleg","Nazarov") #создали лектора
lector1.addCourses() #добавили ему курс

print()

pupil1=Student("Azat","Abdrashitov","M") #создали студента
pupil1.courses_in_progress.append("GIT") #добавили курс студенту
pupil1.finished_courses.append("Python") # добавили завершенный курс
pupil1.gradeLecturer(lector1) #оценка 1
pupil1.gradeLecturer(lector1) #оценка 2

print()

homework1=Reviewers("Boris","Trushin")
homework1.courses_attached.append("GIT")
homework1.rate_hw(pupil1,"GIT",8)


print(lector1) #Инфа о лекторе
print(homework1)
print(pupil1)






























##def main():
##    getChoice=None
##    while getChoice!="q":
##        print("""
##            s - add student
##            l - add lecturer
##            aG - student gives a grade to the lecturer
##            aCS - add course to the student
##            aCL - add course to the lecturer
##            look - print()
##            """)
##        getChoice=input("Выбор:")
##        if getChoice=="s":
##            name=input("Имя студента:")
##            surname=input("Фамилия студента:")
##            gender=input("Гендер студента:")
##            pupil=Student(name,surname,gender)
##        elif getChoice=="l":
##            name=input("Имя лектора:")
##            surname=input("Фамилия лектора:")
##            teacher=Lecturer(name,surname)
##        elif getChoice=="aCS":
##            course=input("Добавить курс:")
##            pupil.courses_in_progress.append(course)
##        elif getChoice=="aCL":
##            course=teacher.addCourses()
##            teacher.courses_attached.append(course)
##        elif getChoice=="aG":
##            getLecurer=list(map(str, input("Имя/Фамилия лектора:").split()))
##            if getLecurer[0]==teacher.name and getLecurer[1]==teacher.surname:
##                pupil.gradeLecturer(teacher)
##            else:
##                print("Такого лектора не сущесвует!")
##        elif getChoice=="look":
##            print(pupil.name,pupil.surname)
##            print(teacher.name,teacher.surname)
##            print(teacher.grade_lecturer)
##
##main()
####teacher1=Lecturer("Oleg","Nazarov")
####a=teacher1.addCourses()
####teacher1.courses_attached.append(a)
####
####pupil1=Student("Azat","Abdrashitov","M")
####b=input("Введите название курса:")
####pupil1.courses_in_progress.append(b)
####pupil1.gradeLecturer(teacher1)
####print(teacher1.grade_lecturer)