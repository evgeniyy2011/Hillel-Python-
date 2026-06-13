class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"Name:{self.first_name}\n Last name:{self.last_name}\n Age:{self.age}, Gender:{self.gender}"

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender,age,first_name,last_name)
        self.r_book = record_book

    def __str__(self):
        return f"{super().__str__()}\n record_book:{self.r_book}"

class ManyPeople(Exception):
    pass

class Group():

    def __init__(self, number):
        self.number = number
        self.group = set()


    def add_student(self, student):
        if len(self.group) >= 10:
            raise ManyPeople("You can't add more then 10 students")
        self.group.add(student)


    def delete_student(self, last_name):
        stud = self.find_student(last_name)
        if stud is not None:
            self.group.discard(stud)


    def find_student(self, last_name):
        for i in self.group:
            if i.last_name == last_name:
                return i
        return None

    def __str__(self):
        all_students = ''
        for i in self.group:
            all_students+= str(i) + "\n"
        return f'Number:{self.number}\n {all_students} '

gr = Group('PD1')
st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 21, 'John', 'Smith', 'AN146')
st4 = Student('Male', 22, 'Tom', 'Brown', 'AN147')
st5 = Student('Female', 23, 'Anna', 'White', 'AN148')
st6 = Student('Male', 24, 'Jack', 'Black', 'AN149')
st7 = Student('Female', 25, 'Kate', 'Green', 'AN150')
st8 = Student('Male', 26, 'Bob', 'Stone', 'AN151')
st9 = Student('Female', 27, 'Mary', 'Wood', 'AN152')
st10 = Student('Male', 28, 'Nick', 'Fox', 'AN153')
st11 = Student('Female', 29, 'Sara', 'Wolf', 'AN154')
try:
    gr.add_student(st1)
    gr.add_student(st2)
    gr.add_student(st3)
    gr.add_student(st4)
    gr.add_student(st5)
    gr.add_student(st6)
    gr.add_student(st7)
    gr.add_student(st8)
    gr.add_student(st9)
    gr.add_student(st10)
    gr.add_student(st11)
except ManyPeople as errro:
    print(errro)

print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод пошуку повинен повертати екземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!
