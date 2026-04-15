# Inheritance helps in the code reusability
# It is always upwards


class User:
    def login(self):
        print("LOGIN")

    def signup(self):
        print("SIGNUP")


class Student(User):
    def enroll(self):
        print("ENROLLED")

    def course(self):
        print("All course")


stu1 = Student()

stu1.course()
stu1.login()
stu1.signup()
