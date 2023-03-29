"""A university wants to automate their admission process. Students are admitted based on marks scored in a qualifying exan
A student is identified by student id, age and marks in
qualifying exan
Data are valid, if:
Age is greater than 20
Marks is between 0 and 100 (both inclusive)
A student qualifies for admission, if Age and marks are valid and Marks is 65 or more
Write a python program to represent the students seeking admission in the university.
RULES TO FOLLOW:
The details of student class are given below.
Class name: Student
Attributes:(private)
student id
marks
age
Methods
(public)
validate marks()
validate age()
check qualification()
__init__() Create and initialize all instances If data is valid, return true. Else, no
Validate marks and age.
If valid, check if marks is 65 or more.
If so return true
Else return false
Else return false
setter methods Include setter methods for all instance
variables to set its values getter methods Include getter methods for all instance variab
Continuing with the previous scenario, a student eligible for. If they have scored more
than 85 marks in qualifying exam, the
Valid course ids and fees are given below:
"""
class Student:
    def _init_(self):
        self.__student_id=None
        self.__marks=None
        self.__age=None
    def set_marks(self,marks):
        self.__marks=marks
    def set_age(self,age):
        self.__age=age
    def set_student_id(self,student_id):
        self.__student_id=student_id
 
    def get_student_id(self):
        return self.__student_id
    def get_marks(self):
        return self.__marks
    def get_age(self):
        return self.__age

    def validate_age(self):
        return self.__age > 20
    def validate_marks(self):
        return 0<=self.__marks<=100
    
    def check_qualification(self):
        return self.validate_marks() and self.validate_age() and self.__marks>=65
"""class Student:
    def __init__(self):
        self.stud_id=None
        self.marks=None
        self.age=None
        self.fees=None
        self.c_id=None
    def get_stud_id(self):
        return self.stud_id
    def set_stud_id(self,stud_id):
        self.stud_id=stud_id
    def get_marks(self):
        return self.marks
    def set_marks(self,marks):
        self.marks=marks
    def get_age(self):
        return self.age
    def set_age(self,age):
        self.age=age
    def get_fees(self):
        return self.fees
    def set_fees(self,fees):
        self.fees=fees
    
    def get_c_id(self):
        return self.c_id
    def set_c_id(self,c_id):
        self.c_id=c_id
    def validate_age(self,age):
        if self.age>20:
            return True
        else:
            return "Not Eligible"
    def validate_marks(self,marks):
        if self.marks>=0 and self.marks<=100:
            return True
        else:
            return False
    def check_qualification(self,age,marks):
        
        if self.age > 20 and self.marks >65:
                if self.marks>85:
                    self.fees=self.fees*0.75
                
        else:
            print("Not eligible for admission")
    
                       
    def display(self):
        print(self.fees)
s1=Student()
s1.set_age(29)
s1.set_marks(90)
s1.set_fees(10000)
s1.check_qualification()
#s1.check_discount()
s1.display()
s2=Student()
s2.set_age(29)
s2.set_marks(70)
s2.set_fees(10000)
s2.check_qualification()
#s2.check_discount()
s2.display()
s3=Student()
s3.set_age(19)
s3.set_marks(70)
s3.set_fees(10000)
s3.check_qualification()
#s2.check_discount()
s3.display()"""


    
