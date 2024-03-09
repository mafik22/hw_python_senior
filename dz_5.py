class Parent1:
    def __init__(self):
        self.parent1_attribute = "Parent 1 attribute"

    def parent1_method(self):
        return "This is a method from Parent 1"


class Parent2:
    def __init__(self):
        self.parent2_attribute = "Parent 2 attribute"

    def parent2_method(self):
        return "This is a method from Parent 2"


class Child(Parent1, Parent2):
    def __init__(self):
        super().__init__()


    def child_method(self):
        return "This is a method from Child"

child_obj = Child()
print(child_obj.parent1_attribute)
print(child_obj.parent1_attribute)
print(child_obj.parent1_method())
print(child_obj.parent1_method())
print(child_obj.child_method())
