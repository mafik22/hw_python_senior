class Student:
    def __init__(self, name, grade, money):
        self.name = name
        self.grade = grade
        self.money = money

    def study(self, hours):
        if self.grade + hours * 0.1 <= 12:
            self.grade += hours * 0.1
        else:
            self.grade = 12

    def work(self, cash):
        self.money += cash * 2

    def get_money(self):
        return self.money

    def relax(self, hours):
        if self.money >= hours * 5:
            self.money -= hours * 5
        else:
            print("Не вистачає коштів на розваги. Йди на роботу.")

    def play(self, hours):
        if self.grade >= hours * 0.2:
            self.grade -= hours * 0.2
        else:
            print("Дуже маленька оцінка. Іди вчись.")

    def get_grade(self):
        return self.grade


def simulate_year(student):
    for month in range(1, 13):
        print(f"Місяць {month}:")
        lesson = float(input("Повчи його - "))
        student.study(lesson)

        game = float(input("Пограй з ним - "))
        student.play(game)

        have_fun = float(input("Повідихай - "))
        student.relax(have_fun)

        job = float(input("поработай - "))
        student.work(job)

        print(f"Оцінка {student.name}: {student.get_grade()} | Гроші: {student.get_money()}$")

student = Student("Вася", 1, 50)

simulate_year(student)
