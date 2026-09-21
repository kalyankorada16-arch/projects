class Person:
    university_name = "Codegnan University"   # Class Attribute

    def __init__(self, name, age, Edu_BG, Gender, Department):
        self.name = name
        self.age = age
        self.Edu_BG = Edu_BG
        self.Gender = Gender
        self.Department = Department

    def display_info(self):
        """Method to be overridden"""
        pass


# ---------------- Student ---------------- #

class Student(Person):
    student_count = 0

    def __init__(self, name, age, student_id, course, Year_, Edu_BG, Gender, Department):
        super().__init__(name, age, Edu_BG, Gender, Department)

        self.__student_id = student_id
        self.course = course
        self.Year_ = Year_

        Student.student_count += 1

    def display_info(self):
        print("\n------ Student Details ------")
        print("University :", Person.university_name)
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Student ID :", self.__student_id)
        print("Course     :", self.course)
        print("Year       :", self.Year_)
        print("Education  :", self.Edu_BG)
        print("Gender     :", self.Gender)
        print("Department :", self.Department)

    def get_student_id(self):
        return self.__student_id

    @classmethod
    def total_students(cls):
        print("Total Students :", cls.student_count)


# ---------------- Faculty ---------------- #

class Faculty(Person):
    faculty_count = 0

    def __init__(self, name, age, faculty_id, Department, Edu_BG, Gender):
        super().__init__(name, age, Edu_BG, Gender, Department)

        self.__faculty_id = faculty_id

        Faculty.faculty_count += 1

    def display_info(self):
        print("\n------ Faculty Details ------")
        print("University :", Person.university_name)
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Faculty ID :", self.__faculty_id)
        print("Education  :", self.Edu_BG)
        print("Gender     :", self.Gender)
        print("Department :", self.Department)

    @staticmethod
    def university_policy():
        print("\nUniversity Policy:")
        print("Codegnan University follows strict academic policies.")

    @classmethod
    def total_faculty(cls):
        print("Total Faculty Members :", cls.faculty_count)


# ---------------- Librarian ---------------- #

class Librarian(Person):
    librarian_count = 0

    def __init__(self, name, age, librarian_id, Edu_BG, Gender, Department):
        super().__init__(name, age, Edu_BG, Gender, Department)
        self.__librarian_id = librarian_id
        Librarian.librarian_count += 1

    def display_info(self):
        print("\n------ Librarian Details ------")
        print("University :", Person.university_name)
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Librarian ID :", self.__librarian_id)
        print("Education  :", self.Edu_BG)
        print("Gender     :", self.Gender)
        print("Department :", self.Department)

    @classmethod
    def total_librarians(cls):
        print("Total Librarians :", cls.librarian_count)


# ---------------- Bus Driver ---------------- #

class BusDriver(Person):
    driver_count = 0

    def __init__(self, name, age, driver_id, bus_no, Edu_BG, Gender, Department):
        super().__init__(name, age, Edu_BG, Gender, Department)
        self.__driver_id = driver_id
        self.bus_no = bus_no
        BusDriver.driver_count += 1

    def display_info(self):
        print("\n------ Bus Driver Details ------")
        print("University :", Person.university_name)
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Driver ID  :", self.__driver_id)
        print("Bus Number :", self.bus_no)
        print("Education  :", self.Edu_BG)
        print("Gender     :", self.Gender)
        print("Department :", self.Department)

    @classmethod
    def total_drivers(cls):
        print("Total Bus Drivers :", cls.driver_count)


# ---------------- Cleaning Staff ---------------- #

class CleaningStaff(Person):
    cleaner_count = 0

    def __init__(self, name, age, cleaner_id, shift, Edu_BG, Gender, Department):
        super().__init__(name, age, Edu_BG, Gender, Department)
        self.__cleaner_id = cleaner_id
        self.shift = shift
        CleaningStaff.cleaner_count += 1

    def display_info(self):
        print("\n------ Cleaning Staff Details ------")
        print("University :", Person.university_name)
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Cleaner ID :", self.__cleaner_id)
        print("Shift      :", self.shift)
        print("Education  :", self.Edu_BG)
        print("Gender     :", self.Gender)
        print("Department :", self.Department)

    @classmethod
    def total_cleaners(cls):
        print("Total Cleaning Staff :", cls.cleaner_count)


# ---------------- Technical Staff ---------------- #

class TechnicalStaff(Person):
    technical_count = 0

    def __init__(self, name, age, emp_id, specialization, Edu_BG, Gender, Department):
        super().__init__(name, age, Edu_BG, Gender, Department)
        self.__emp_id = emp_id
        self.specialization = specialization
        TechnicalStaff.technical_count += 1

    def display_info(self):
        print("\n------ Technical Staff Details ------")
        print("University :", Person.university_name)
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Employee ID:", self.__emp_id)
        print("Specialization :", self.specialization)
        print("Education  :", self.Edu_BG)
        print("Gender     :", self.Gender)
        print("Department :", self.Department)

    @classmethod
    def total_technical_staff(cls):
        print("Total Technical Staff :", cls.technical_count)


# ---------------- Non Technical Staff ---------------- #

class NonTechnicalStaff(Person):
    nontech_count = 0

    def __init__(self, name, age, emp_id, designation, Edu_BG, Gender, Department):
        super().__init__(name, age, Edu_BG, Gender, Department)
        self.__emp_id = emp_id
        self.designation = designation
        NonTechnicalStaff.nontech_count += 1

    def display_info(self):
        print("\n------ Non Technical Staff Details ------")
        print("University :", Person.university_name)
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Employee ID:", self.__emp_id)
        print("Designation:", self.designation)
        print("Education  :", self.Edu_BG)
        print("Gender     :", self.Gender)
        print("Department :", self.Department)

    @classmethod
    def total_nontechnical_staff(cls):
        print("Total Non Technical Staff :", cls.nontech_count)




# ---------------- Objects ---------------- #

student1 = Student("Rahul Sharma",21,"CNU12345","Computer Science",2026,"Intermediate","Male","IT")

student2 = Student("Ananya Reddy",22,"CNU67890","Data Science",2026,"Intermediate","Female","IT")

faculty1 = Faculty("Dr. Ravi Kumar",45,"F001","AI & ML","PhD","Male")

faculty2 = Faculty("Dr. Meera Srinivas",50,"F002","Cybersecurity","PhD","Female")

librarian1 = Librarian("Shankar", 40, "L001", "M.Lib", "Male", "Library")
librarian2 = Librarian("Rohit", 35, "L002", "M.Lib", "Female", "Library")

driver1 = BusDriver("Chaitnya", 45, "D001", "AP39AB1234", "10th", "Male", "Transport")
driver2 = BusDriver("Ganesh", 40, "D002", "AP39AB1444", "Intermediate", "Male", "Transport")

cleaner1 = CleaningStaff("kalyan", 38, "C001", "Morning", "10th", "Female", "Maintenance")
cleaner2 = CleaningStaff("kamala", 41, "C002", "Afternoon", "9th", "Female", "Maintenance")

technical1 = TechnicalStaff("vijay", 30, "T001", "Network Engineer", "B.Tech", "Male", "IT Support")
technical2 = TechnicalStaff("arjun", 29, "T002", "Office Clerk", "B.Tech", "Male", "IT Support")


nontech1 = NonTechnicalStaff("raji", 35, "NT001", "Office Assistant", "B.Com", "Female", "Administration")
nontech2 = NonTechnicalStaff("kavi", 38, "NT002", "Office Boy", "Intermediate", "Male", "Administration")


# ---------------- Output ----------------  #

student1.display_info()
student2.display_info()

print("\nStudent ID:", student1.get_student_id())

faculty1.display_info()
faculty2.display_info()

Faculty.university_policy()

Student.total_students()
Faculty.total_faculty()

librarian1.display_info()
librarian2.display_info()

driver1.display_info()
driver2.display_info()

cleaner1.display_info()
cleaner2.display_info()

technical1.display_info()
technical2.display_info()

nontech1.display_info()
nontech2.display_info()


print()

Faculty.total_faculty()
Librarian.total_librarians()
BusDriver.total_drivers()
CleaningStaff.total_cleaners()
TechnicalStaff.total_technical_staff()
NonTechnicalStaff.total_nontechnical_staff()


























