class Person:
    def __init__(self,name, age, hometown):
        self.name = name
        self.age = age
        self.hometown = hometown

    def bio(self):
        print("I am {} and I am {} years old, I grew up in {}.".format(self.name, self.age, self.hometown))

p1 = Person("nat", 23, "bogota")
print(p1.bio())
print(p1.age)