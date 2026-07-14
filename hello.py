class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return "Woof!"
        
jerry = Dog(name="jerry")

jerry.name
jerry.bark()
