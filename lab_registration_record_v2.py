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
        self.__f_name = f_name
        self.__l_name = l_name
        self.__study_type = study_type
        self.__courses = []

    # def __str__(self):
    #     return f"{self.student_name} {self.study_type} {self.courses}"

    # Method within the Class Student to return Student information
    @property
    def student_name(self):
        return self.__f_name, self.__l_name

    @student_name.setter
    def student_name(self, fname, lname):
        # Error checking for name to be a string and not a number
        if self.__l_name.isdigit() or self.__f_name.isdigit():
                print("You cannot enter a number as a student name")
        else:
            self.__f_name = fname
            self.__l_name = lname

    @property
    def study_type(self):
        return self.__study_type

    @study_type.setter
    def study_type(self, value):
        # ERROR checking for wrong type of variables entered for Student info
        if value not in (Student.POSTGRADUATE, Student.UNDERGRADUATE):
            raise ValueError

    @property
    def courses(self):
        return self.__courses

    @courses.setter
    def courses(self, value):
        return self.__courses.append(value)


    def get_all_student_data(self):
        return self.student_name, self.study_type, self.courses


class RegistrationData:
    """
    In this Class Information about the students registered and is given
    to the methods and then displayed in the method called display_student_data
    """
    # initialization Method
    def __init__(self, address, registration_fee, study_type, f_name, l_name, s_id="NA"):
        self.__address = address
        self.__registration_fee = registration_fee
        self.__s_id = s_id
        self.__student_obj = Student(study_type, f_name, l_name)

    @property
    def address_property(self):
        return self.__address

    @address_property.setter
    def address_property(self, value):
        self.__address = value

    @property
    def student_id_property(self):
        return self.__s_id

    @student_id_property.setter
    def student_id_property(self, value):
        self.__s_id = value

    @property
    def registration_fee_property(self):
        return self.__registration_fee

    @registration_fee_property.setter
    def registration_fee_property(self, value):
        self.__registration_fee = value

    @property
    def student_object_property(self):
        return self.__student_obj

    @student_object_property.setter
    def student_object_property(self, value):
        self.__student_obj = value

    # Method to display all information of the students including registration
    def display_student_data(self):
        print("Student Info: ", self.student_object_property.get_all_student_data(), self.student_id_property)
        print("Address: ", self.address_property)
        print("Registration fee: ", self.registration_fee_property)

r = RegistrationData("8 Lower Kevin Street, Dublin 8, Ireland", 1500, Student.POSTGRADUATE, "Bianca", "Phelan")
r.display_student_data()
r.student_id_property="C12345"
r.display_student_data()
for course in ("OOP", "Advanced Databases", "Environmental Analytics"):
    r.student_object_property.courses = course
r.display_student_data()

# Creating documentation for both classes
# print(Student.__doc__)
# print(RegistrationData.__doc__)