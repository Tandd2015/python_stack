# define class User
class User:
    # this method to run every time a new object is instantiated
    def __init__(self, name, email):
	# instance attributes 
        self.name = name
        self.email = email
        self.logged = True
        print(f"{self.name} has been created!")
    # login method changes the logged status for a single instance (the instance calling the method)
    def login(self):
        self.logged = True
        print(self.name + " is logged in.")
        return self
    # logout method changes the logged status for a single instance (the instance calling the method)
    def logout(self):
        self.logged = False
        print(self.name + " is not logged in")
        return self
    # print name and email of the calling instance
    def show(self):
        print(f"My name is {self.name}. You can email me at {self.email}.")
        return self
    def sayHello(self, User):
        print(f"{self.email} says hello to {User.email}!")
        return self

# Mike = User("Michael", "mike@mail.com")
# Dan = User("Daniel", "dan@mail.com")
# Mike.login().show().sayHello(Dan).logout()


class Hero:
    #give Hero health, attack, name
    def __init__(self, attack, name):
        self.health = 500
        self.attack = attack
        self.name = name
        self.location = 0
        print(f"Hero {self.name} has arrived!")
    def moveLeft(self):
        self.location-=1
        print(f"You have moved, you are now located at {self.location}")
        return self
    def moveRight(self):
        self.location+=1
        return self
    def basicAttack(self, Target):
        print(f"You have moved, you are now located at {self.location}")
        Target.health -= self.attack
        print(f"Hero {self.name} attacks {Target.name} and inflicts {self.attack} damage!")
        if(Target.health <= 0):
            print(f"{Target.name} has been destroyed")
        return self
class Ninja(Hero):
    def sneak(self):
        self.health = 300
        print(f"No one saw {self.name}")
        return self
class Wizard(Hero):
    def heal(self, Target):
        Target.health += self.attack
        print(f"{self.name} healed {Target.name} for {self.attack} points!")
        return self


class Grunt:
    def __init__(self, attack, name):
        self.health = 200
        self.attack = attack
        self.name = name
        print(f"Grunt {self.name} has been created")
    def basicAttack(self, Target):
        Target.health -= self.attack
        print(f"Grunt {self.name} attacks {Target.name} and inflicts {self.attack} damage!")


Hercules = Hero(200, "Hercules")
Grunt = Grunt(50, "Grunt")
Melvin = Wizard(300, "Melvin")
Choi = Ninja(300, "Choi")
Choi.sneak()
print(Choi.health)

Hercules.moveLeft().moveLeft().moveLeft().moveRight().basicAttack(Grunt)
Melvin.heal(Grunt).heal(Grunt)

print(Grunt.health)

# class Vehicle:
#     def __init__(self, wheels, capacity, make, model):
#         self.wheels = wheels
#         self.capacity = capacity
#         self.make = make
#         self.model = model
#         self.mileage = 0
#     def drive(self,miles):
#         self.mileage += miles
#         return self
#     def reverse(self,miles):
#         self.mileage -= miles
#         return self
# class Bike(Vehicle):
#     def vehicle_type(self):
#         return "Bike"
# class Car(Vehicle):
#     def set_wheels(self):
#         self.wheels = 4
#         return self
# class Airplane(Vehicle):
#     def fly(self, miles):
#         self.mileage += miles
#         return self
# v = Vehicle(4,8,"dodge","minivan")
# print(v.make)
# b = Bike(2,1,"Schwinn","Paramount")
# print(b.vehicle_type())
# c = Car(8,5,"Toyota", "Matrix")
# c.set_wheels()
# print(c.wheels)
# a = Airplane(22,853,"Airbus","A380")
# a.fly(580)
# print(a.mileage)