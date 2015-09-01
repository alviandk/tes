class Student:

    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.uang_jajan=100
        
    def say_name(self):
        print('My name is {}'.format(self.name))
    def say_age(self):
        print('I am {} years old'.format(self.age))
