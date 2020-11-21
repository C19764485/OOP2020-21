# course: Object-oriented programming, year 2, semester 1
# academic year: 2020-21
# author: Panagiotis Bampilis
# date: 21-11-2020

class Student:
    """
    Here is where the initialization is been made for
    the students basic information. The information is passed to
    the next method called "student_info" below
    """
    # Declaring global variable scope for study type
    UNDERGRADUATE, POSTGRADUATE = range(2)

    # initialization Method
    def __init__(self, study_type, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name
        self.study_type = study_type
        study_type = Student.UNDERGRADUATE or Student.POSTGRADUATE
        self.courses = []
        #
        # ERROR checking for wrong type of variables entered for Student info
        try:
            if self.study_type > 1 or self.study_type < 0:
                print("You must enter between Postgraduate and Undergraduate")
        except ValueError:
            print("Not a valid study type: ", self.study_type)
        try:
            if self.l_name.isdigit() or self.f_name.isdigit():
                print("You cannot enter a number as a student name")
        except ValueError:
            print("Entered wrong type of variable")
        except AttributeError:
            print("Entered wrong type of variable")

    # Method within the Class Student to return Student information
    def student_info(self):
        return self.f_name, self.l_name

    # Created a method to return Study types
    def study_types(self):
        return self.study_type

    # Created a method to return Courses
    def course(self):
        return self.courses

class RegistrationData:
    """
    In this Class Information about the students registered and is given
    to the methods and then displayed in the method called display_student_data
    """
    # initialization Method
    def __init__(self, address, registration_fee, study_type, f_name, l_name, s_id="NA"):
        self.address = address
        self.registration_fee = registration_fee
        self.s_id = s_id
        self.student_object = Student(study_type, f_name, l_name)

    # Created a method to return Student id
    def student_id_property(self):
        return self.s_id

    # Method to display all information of the students including registration
    def display_student_data(self):
        print("Student Info: ", self.student_object.student_info(), self.student_object.study_types(), self.student_object.course(), RegistrationData.student_id_property(self)) ######################
        print("Address: ", self.address)
        print("Registration fee: ", self.registration_fee)

r = RegistrationData("8 Lower Kevin Street, Dublin 8, Ireland", 1500, Student.POSTGRADUATE, "Bianca", "Phelan")
r.display_student_data()
r.student_id_property="C12345"
r.display_student_data()
for course in ("OOP", "Advanced Databases", "Environmental Analytics"):
    r.student_object.courses = course
r.display_student_data()

# Creating documentation for both classes
print(Student.__doc__)
print(RegistrationData.__doc__)