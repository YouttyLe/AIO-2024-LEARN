class Student:
    def __init__(self, name, yob, grade):
        self.name = name
        self.yob = yob
        self.grade = grade

    def describe(self):
        print(f"Student - Name: {self.name} - YoB: {self.yob} - Grade: {self.grade}")


class Teacher:
    def __init__(self, name, yob, subject):
        self.name = name
        self.yob = yob
        self.subject = subject

    def describe(self):
        print(f"Teacher - Name: {self.name} - YoB: {self.yob} - Subject: {self.subject}")


class Doctor:
    def __init__(self, name, yob, specialist):
        self.name = name
        self.yob = yob
        self.specialist = specialist

    def describe(self):
        print(f"Doctor - Name: {self.name} - YoB: {self.yob} - Specialist: {self.specialist}")


class Ward:
    def __init__(self, name):
        self.name = name
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def describe(self):
        print(f"Ward Name: {self.name}")
        for person in self.people:
            person.describe()

    def count_doctor(self):
        count = 0
        for person in self.people:
            if isinstance(person, Doctor):
                count += 1
        return count

    def sort_age(self):
        self.people.sort(key=lambda x: x.yob)

    def compute_average(self):
        teacher_yobs = [person.yob for person in self.people if isinstance(person, Teacher)]
        if len(teacher_yobs) > 0:
            return sum(teacher_yobs) / len(teacher_yobs)
        else:
            return None


def create_person(person_type):
    name = input(f"Name: {person_type}: ")
    yob = int(input(f"YoB {person_type}: "))

    if person_type.lower() == "student":
        grade = input(f"Grade {person_type}: ")
        return Student(name, yob, grade)

    elif person_type.lower() == "teacher":
        subject = input(f"Subject {person_type}: ")
        return Teacher(name, yob, subject)

    elif person_type.lower() == "doctor":
        specialist = input(f"specialist: {person_type}: ")
        return Doctor(name, yob, specialist)

    else:
        print("Error!")
        return None


def main():
    ward_name = input("enter Ward: ")
    ward = Ward(ward_name)

    while True:
        print("Selection:")
        print("1. Student")
        print("2. Teacher")
        print("3. Doctor")
        print("4. Finish")

        choice = input("choose (1-4): ")

        if choice == '1':
            ward.add_person(create_person("student"))
        elif choice == '2':
            ward.add_person(create_person("teacher"))
        elif choice == '3':
            ward.add_person(create_person("doctor"))
        elif choice == '4':
            break
        else:
            print("Enter again.")

    ward.describe()
    print()
    print(f"Number of doctors: {ward.count_doctor()}")
    ward.sort_age()
    print()
    ward.describe()
    print()
    print(f"Average year of birth: {ward.compute_average()}")


if __name__ == "__main__":
    main()
