class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self
    
    def run(self):
        self.health -= 5
        return self

    def display_health(self):
        print "The animals health is " + str(self.health)
        return self 
animal1 = Animal("panda", 100)
animal1.walk().walk().walk().run().run().display_health()

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(self, name)
        self.health = 150

    def pet(self):
        self.health += 5
        return self
animal2 = Dog("dog")
animal2.walk().walk().walk().run().run().pet().display_health()

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(self, name)
        self.health = 170

    def fly(self):
        self.health -= 10
        return self
    def display_health(self):
        print "I am a Dragon"
        super(Dragon, self).display_health()
        return self
animal3 = Dragon("dragon")
animal3.display_health()

animal4 = Animal("lion", 170)
# animal4.pet().fly()
animal4.display_health()

animal5 = Dog("dog")
# animal5.fly()



