class Human:
    def __init__(self, name: str = "Sim", age: int = 0, energy: int = 100, hapiness: int = 100, hunger = 100):
        self.name = name
        self.age = age
        self.energy = energy
        self.happiness = hapiness
        self.hunger = hunger
    def eat(self, food: int):
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        print(f"{self.name} ate. Hunger: {self.hunger}")
    def sleep(self, hours: int):
        self.energy += hours
        if self.energy > 100:
            self.energy = 100
        print(f"{self.name} slept. energy: {self.energy}")
    def play(self, activity: int):
        self.energy += activity
        if self.energy > 100:
            self.energy = 100
        print(f"{self.name} played. hapiness: {self.happiness}")
    def age_up(self, years: int = 1):
        self.age += years
        print(f"{self.name} aged up. Age: {self.age}")
    def status(self):
        print(f"{self.name}'s Status - Age: {self.age}, Energy: {self.energy}, Happiness: {self.happiness}, Hunger: {self.hunger}")
class dog:
    def __init__(self, name: str = "rock", age: int= 1, energy: int = 100, happiness: int = 100, hunger: int = 100):
        self.name = name
        self.age = age
        self.energy = energy
        self.happiness = happiness
        self.hunger = hunger
    def eat(self, food: int):
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        print(f"{self.name} ate. Hunger: {self.hunger}")
    def sleep(self, hours: int):
        self.energy += hours
        if self.energy > 100:
            self.energy = 100
        print(f"{self.name} slept. energy: {self.energy}")
    def play(self, activity: int):
        self.energy += activity
        if self.energy > 100:
            self.energy = 100
        print(f"{self.name} played. hapiness: {self.happiness}")
    def age_up(self, years: int = 1):
        self.age += years
        print(f"{self.name} aged up. Age: {self.age}")
    def status(self):
        print(f"{self.name}'s Status - Age: {self.age}, Energy: {self.energy}, Happiness: {self.happiness}, Hunger: {self.hunger}")
class car:
    def __init__(self, name: str = "mercedes", age: int= 1, fuel: int = 100, repair: int = 100, cleanliness: int = 100):
        self.name = name
        self.age = age
        self.fuel = fuel
        self.repair = repair
        self.cleanliness = cleanliness
    def refueling(self, fuel: int):
        self.fuel -= fuel
        if self.fuel < 0:
            self.fuel = 0
        print(f"{self.name} refueling. fuel: {self.fuel}")

    def repairing(self, hours: int):
        self.repair += hours
        if self.repair > 100:
            self.repair = 100
        elif self.repair < 20:
            return self.repair
        print(f"{self.name} repair. repairing: {self.repair}")
    def clean (self, activity: int):
        self.cleanliness += activity
        if self.cleanliness > 100:
            self.cleanliness = 100
        print(f"{self.name} clean. cleanliness: {self.cleanliness}")
    def age_up(self, years: int = 1):
        self.age += years
        if self.age > 20:
            return self.age
        print(f"{self.name} aged up. Age: {self.age}")
    def status(self):
        print(f"{self.name}'s Status - Age: {self.age}, Energy: {self.fuel}, Happiness: {self.repair}, Hunger: {self.cleanliness}")

sim1 = Human("Sim1")
sim1.eat(30)
sim1.sleep(8)
sim1.play(20)
sim1.age_up(5)
sim1.status()
dog1 = dog("Dog1")
dog1.eat(30)
dog1.sleep(2)
dog1.play(30)
dog1.age_up(3)
dog1.status()
car2 = car("Mercedes")
car2.fuel(23)
car2.repair(20)
car2.cleanliness(19)
car2.age(10)
car2.status()
