#inheritance
#parent class

class User:

    def __init__(self):
        self.name="Aman"

    def login(self):
        print('login')
#child class
class Student(User):
    def enroll(self):
        print('enroll into the course')

obj=User()
obj1=Student()
print(obj1.name)