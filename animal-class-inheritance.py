class Animal:
    def __init__(self,name, color):
        self.name = name
        self.color = color
    
    def bio(self):
        print("Hi I am {} and {}".format(self.name, self.color))

class Dog(Animal):
    def __init__(self, name, color, breed):
        super().__init__(name, color)
        self.breed = breed

animal1 = Animal("josie", "brown")
animal1.bio()

dog1 = Dog("Troy", "blonde", "golden retriever")
dog1.bio()