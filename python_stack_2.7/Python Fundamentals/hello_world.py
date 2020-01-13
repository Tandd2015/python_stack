
print "Hello World!"

x = "Hello Python"
print x
y = 42
print y

print "this is a sample python string"

name = "python daniel"
print "my name is 42", name

name = "python daniel"
print "my name is 42 " + name

first_name = "python crazy daniel"
last_name = "beatty and i mean crazy python"
print "my name is {} {}".format(first_name, last_name)
'''
""" 
hw = "hello %s" % 'world'
print hw

x = "Hello World"
print x.upper()
print x.count()
print x.endswitch()
print x.find()
print x.isalnum()
print x.isalpha()
print x.isdigit()
print x.islower()
print x.join()
print x.split()
"""

""" ninjas = ['daniel', 'harlow', 'Christina']
armory_list = ['armory_list there_are_backpacks_this_armory', '5', ['ninja_stars', 'katana', 'Kyoketshu-Shogei Knife', 'backpack_list'], 2018]
empty_list = []

ninjas_go = ninjas + armory_list[2]
print ninjas_go

armory_inventory = 5 * armory_list[2]
print armory_inventory
"""

""" 
drawer = ['understanding', 'the', 'concept']
print drawer[0]
print drawer[1]
print drawer[2]
 """

"""
x = [1,2,3,4,5]
x.append([1,2,3,4])
print x
"""

"""
x = [100,99,98,97,96,95]

print x[:]
print x[1:]
print x[:4]
print x[2:4]
"""

"""
my_list = [31, 'daniel', 'hi']
print len(my_list)
print enumerate(my_list)
print map(my_list, my_list)
print min(my_list)
print sorted(my_list)
"""

"""
age = 15
if age >= 18:
    print 'Legal age'
else:
    print 'you are so young!'
"""

"""
age = 17
if age >= 18:
    print 'Legal Age'
elif age == 17:
    print 'you are SEVENTEEN'
else:
    print 'you are so young!'
"""

'''
for count in range(0, 5):
    print "looping -", count

for count in(0, 5):
    print "looping something different -", count

my_dojo  = ['ninja_and_equipment_list', ['armory_list', '5', ['backpack_list', 'ninja_stars', 'katana', 'Kyoketshu-Shogei Knife'], 4, 2018], 'daniel', 'harlow', 'christina', '3_more']
for element in my_dojo:
    print element
'''

'''
count = 0
while count < 5:
    print 'looping - ', count
    count += 1

for val in "string":
    if val == "i":
        break
    print val

for val in "string":
    if val == "i":
        continue
    print val

class EmptyClass:
    pass
for val in "string":
    pass  
'''

'''
x = 3 
y = x
while y > 0:
    print y
    y = y - 1 
else:
    print "final else statement"

x = 3
y = x
while y > 0:
    print y
    y = y - 1 
    if y == 0:
        break
else:
    print "Final else statement"

"""Functions Python"""
def add(a, b):
    x = a + b
    return x
# the return value gets assigned to the "result" variable
result = add(3, 5)
print result # this should print 8

# we've  named the function "add" and we give it two parameters(inputs to the function)
def add1(a, b):
    x = a + b
    return x # we return something (more on this later)
print add1(3, 5) # prints 8

#this function has one parameter(input)
def say_hi(name):
    print "Hi, " + name
# invoking the function passing in one argument
say_hi('Michael')
say_hi('Anna')
say_hi('Eli')

def say_hi1():
    return "Hi"
greeting = say_hi1() # the returned value from say_hi function gets assigned to the "greeting" variable
print greeting # this will output 'Hi'

def add2(a, b):
   x = a + b
   return x
sum1 = add2(4, 6)
sum2 = add2(1, 4)
sum3 = sum1 + sum2

print sum3, sum2, sum1
""" Debugging in Python"""
def multiply(arr, num):
    print arr, num
    for x in range(len(arr)):
        print x
        arr[x] *= num
        print x
        print arr
    return arr
a = [2,4,10,16]
b = multiply(a, 5)
print b 
"""Tuples Python"""
tuple_data = ('physics', 'chemistry', 1997, 2000)
tuple_num = (1, 2, 3, 4, 5)
tuple_letters = "a", "b", "c", "d"

dog = ("Canis Familiaris", "dog", "carnivore", 12)
print dog[2]

for data in dog:
    print data

dog = dog + ("domestic",)
print dog

dog = dog[:3] + ("man's best friend",) + dog[4:]
print dog

x = (1,5,6,9,2)
print len(x)
print max(x)
print sum(x)
print enumerate(x)
# print map(x)
print min(x)
print sorted(x)

# def get_circle_area(r):
#     # Return (circumference, area) of a circle of a radius r
#     c = 2 * math.pi * r
#     a = math.pi * r * r
#     return (c, a)
# get_circle_area(20)
# # some type of error with math variable not being defined needs adjustment for use

# English will always be at index 0, French at index 1, and Spanish at index 2. :(Language translater):
import language
print language.translate(dog)
# Some type of error that will not allow the import language i assume it has to deal with a prebuilt function with the thre languages
"""Dictionaries"""
weekend = {"Sun": "Sunday", "Sat": "Saturday"} # literal notation
capitals = {} # create an empty dictionary then add values
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"
print capitals
print weekend
print weekend["Sun"]
print capitals["svk"]

# to print all keys
for data in capitals:
    print data
# another way to print all keys
for key in capitals.iterkeys():
    print key
# to print the values
for val in capitals.itervalues():
    print val
# to print all keys and values
for key,data in capitals.iteritems():
    print key, " = ", data
# Standalone functions
# print cmp(dict1, dict2)
print len(capitals)
print str(capitals)
print type(capitals)
#Dicationary methods { /dict.method(yourDictionary)/ and /yourDictionary.method()/ }
# .clear()
# .copy()
# .fromkeys(sequence, [value] )
# .get(key, default=None)
# .has_key(key)
# .items()
# .keys()
# .setdefault(key, default=None)
# .update()
# .values()
context = { # nested dictionaries
    'questions': [
        {'id': 1, 'content': 'Why is there a light in the fridge and not in the freezer?'},
        {'id': 2, 'content': 'Why don\'t sheep shrink when it rains?'},
        {'id': 3, 'content': 'Why are they called apartments when they are all stuck together?'},
        {'id': 4, 'content': 'Why do cars drive on the parkway and park on the driveway?'}
    ]
}
for key, data in context.items():
    # print data
    # print key
    for value in data:
        print "Question #", value["id"], ": ", value["content"]

data = {"house":"Haus", "cat":"Katze", "red":"rot"} # lists from Dictionary
print data.items()
print data.keys()
print data.values()

dishes = ["pizza", "sauerkraut", "paella", "hamburger"] # dictionaries from lists
countries = ["Italy", "Germany", "Spain", "USA"]
counrty_specialities = zip(countries, dishes) # combines the two lists like a zipper
print counrty_specialities
counrty_specialities_dict = dict(counrty_specialities) # transforms last form into a real dictionary
print counrty_specialities_dict 
