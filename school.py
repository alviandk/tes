class Student:

    total_student=0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.total_student += 1

    def say_name(self):
        print ("Hi my name is {0}".format(self.name))


    def say_age(self):
       print"iam {} years old".format(self.age)

    def __str__(self):
        return (self.name)
 
