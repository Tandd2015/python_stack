#--------------------------PRINTING STRINGS--------------------------

# print python 3
print("Python 3's print is a function!")
# print python 2.7print "Python 2.7's print is a statement!"
# print "Python 2.7's print is a statement!"

#-- string literals
print("this is a sample string")

#-- concatenating strings and variables with the print function
name="Zen"
print("My name is", name)
print("My name is " + name)

#-- string interpolation

#- f-strings(litera string interpolation)
first_name="Zen"
last_name="Coder"
age=27
print(f"My name is {first_name} {last_name} and I am {age} years old.")
# output: My name is Zen Coder and I am 27 years old.

#- string.format()
print("My name is {} {} and I am {} years old.".format(first_name,last_name,age))
# output: My name is Zen Coder and I am 27 years old.

#- %-formatting

hw= "Hello %s" % "world" 	# with literal values
py= "I love Python %d" % 3 
print(hw, py)
# output: Hello world I love Python 3
print("My name is %s and I'm %d" % (name, age))		# or with variables
# output: My name is Zen and I'm 27

#-- built-in string methods
x= "hello world"
print(x.title())
# output: "Hello World"

#--------------------------PYTHON SYNTAX--------------------------

#-- indentation and line-endings
x= 10
if x > 50:
    print("bigger than 50")
else:
    print("smaller than 50")

#-- pass
my_string= "Daniel"

class empty_class:
    pass

for val in my_string:
    pass

#--------------------------DATA TYPES--------------------------

#-- Primitive data types - These are the basic building blocks of a language. Most languages have these in common:

#- Boolean Values - Assesses the truth value of something. It has only two values: True and False (note the uppercase T and F)
is_hungry = True
has_freckles = False
#- Numbers - Integers (whole numbers), floating point numbers (commonly known as decimal numbers), and complex numbers
age = 35 # storing an int
weight = 160.57 # storing a float
#- Strings - literal text
name = "Joe Blue"

#-- Composite types - These are collections composed of the above primitive types.

#- Tuples - A type of data that is immutable (can't be modified after its creation) and can hold a group of values. Tuples can contain mixed data types.
dog = ('Bruce', 'cocker spaniel', 19, False)
print(dog[0])		# output: Bruce
dog[1] = 'dachshund'	# ERROR: cannot be modified ('tuple' object does not support item assignment)

#- Lists - A type of data that is mutable and can hold a group of values. Usually meant to store a collection of related data.
empty_list = []
ninjas = ['Rozen', 'KB', 'Oliver']
print(ninjas[2]) 	# output: Oliver
ninjas[0] = 'Francis'
ninjas.append('Michael')
print(ninjas)	# output: ['Francis', 'KB', 'Oliver', 'Michael']
ninjas.pop()
print(ninjas)	# output: ['Francis', 'KB', 'Oliver']
ninjas.pop(1)
print(ninjas)	# output: ['Francis', 'Oliver']

#- Dictionaries - A group of key-value pairs. Dictionary elements are indexed by unique keys which are used to access values.
empty_dict = {}
new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
new_person['name'] = 'Jack'	# updates if the key exists
new_person['hobbies'] = ['climbing', 'coding']	# adds a key-value pair if the key doesn't exist
print(new_person)	
# output: {'name': 'Jack', 'age': 38, 'weight': 160.2, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}
w = new_person.pop('weight')	# removes the specified key and returns the value
print(w)		# output: 160.2
print(new_person)	
# output: {'name': 'Jack', 'age': 38, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}    

#-- Common Functions
print(type(2.63))		# output: <class 'float'>
print(type(new_person))		# output: <class 'dict'>

print(len(new_person))		# output: 4 (the number of key-value pairs)
print(len('Coding Dojo'))	# output: 11

#-- Type Casting or Explicit Type Conversion
print("Hello" + 42)			# output: TypeError
print("Hello" + str(42))		# output: Hello 42

total = 35
user_val = "26"
total = total + user_val		# output: TypeError
total = total + int(user_val)		# total will be 61

#--------------------------CONDITIONAL STATEMENTS--------------------------
#-- Conditional statements allow us to run certain lines of code depending on whether certain conditions are met.

x = 12
if x > 50:
    print("bigger than 50")
else:
    print("smaller than 50")
# because x is not greater than 50, the second print statement is the only one that will execute

x = 55
if x > 10:
    print("bigger than 10")
elif x > 50:
    print("bigger than 50")
else:
    print("smaller than 10")
# even though x is greater than 10 and 50, the first true statement is the only one that will execute, so we will only see 'bigger than 10'

if x < 10:
    print("smaller than 10")
# nothing happens, because the statement is false   

#--------------------------FOORLOOPS--------------------------

#-- For Loops with Range
for x in range(0, 10, 1):
    print(x)
for x in range(0, 10):	# increment of +1 is implied
    print(x)
for x in range(10):	# increment of +1 and start at 0 is implied
    print(x)

for x in range(0, 10, 2):
    print(x)
# output: 0, 2, 4, 6, 8
for x in range(5, 1, -3):
    print(x)
# output: 5, 2

#-- For Loops through Lists
my_list = ["abc", 123, "xyz"]
for i in range(0, len(my_list)):
    print(i, my_list[i])
# output: 0 abc, 1 123, 2 xyz  

for v in my_list:
    print(v)
# output: abc, 123, xyz

#-- For Loops through Dictionaries
my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(k)
# output: name, language

my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(my_dict[k])
# output: Noelle, Python

# another way to iterate through the keys
for key in capitals.keys():
     print(key)
#to iterate through the values
for val in capitals.values():
     print(val)
#to iterate through both keys and values
for key, val in capitals.items():
     print(key, " = ", val)

#-- While Loops

#-While - loops are another way of looping while a certain condition is true.
for count in range(0,5):
    print("looping - ", count)

count = 0
while count < 5:
    print("looping - ", count)
    count += 1

# while <expression>:
    # do something, including progress towards making the expression False. Otherwise we'll never get out of here!

#- Else - There are certain conditions that we give for every loop that we have, but what if the condition was not met and we still would like to do something if that happens? We can then use an else statement with our while loop.
y = 3
while y > 0:
    print(y)
    y = y - 1
else:
    print("Final else statement")

#-- Loop Control - We were introduced to control flow in the previous tabs with if and else statements. Loops, breaks, and continues are all a part of control flow as well.

#- Break - The break statement exits the current loop prematurely, resuming execution at the first post-loop statement. The break statement can be used in both while and for loops.
for val in "string":
    if val == "i":
        break
    print(val)
# output: s, t, r

#- Continue - The continue statement immediately returns control to the beginning of the loop. In other words, the continue statement rejects, or skips, all the remaining statements in the current iteration of the loop, and continues normal execution at the top of the loop.
for val in "string":
    if val == "i":
        continue
    print(val)
# output: s, t, r, n, g
# notice, no i in the output, but the loop continued after the i

y = 3
while y > 0:
    print(y)
    y = y - 1
    if y == 0:
        break
else:		# only executes on a clean exit from the while loop (i.e. not a break)
   print("Final else statement")
# output: 3, 2, 1

#--------------------------FUNCTIONS--------------------------
#--Syntax
def add(a,b):	# function name: 'add', parameters: a and b
    x = a + b	# process
    return x	# return value: x

new_val = add(3, 5)    # calling the add function, with arguments 3 and 5
print(new_val)    # the result of the add function gets sent back to and saved into new_val, so we will see 8

#--Parameters and Arguments
def say_hi(name):
    print("Hi, " + name)

# invoking the function 3 times, passing in one argument each time
say_hi('Michael')
say_hi('Anna')
say_hi('Eli')

#--Returning Values
def say_hi(name):
    return "Hi " + name
greeting = say_hi("Michael") # the returned value from say_hi function gets assigned to the 'greeting' variable
print(greeting) # this will output 'Hi Michael'

def add(a, b):
    x = a + b
    return x
sum1 = add(4,6)
sum2 = add(1,4)
sum3 = sum1 + sum2

#--------------------------DEFAULT PARAMETERS--------------------------

def beCheerful(name='', repeat=2):		# set defaults when declaring the parameters
	print(f"good morning {name}\n" * repeat)
beCheerful()				# output: good morning (repeated on 2 lines)
beCheerful("tim")		        # output: good morning tim (repeated on 2 lines)
beCheerful(name="john")			# output: good morning john (repeated on 2 lines)
beCheerful(repeat=6)			# output: good morning (repeated on 6 lines)
beCheerful(name="michael", repeat=5)	# output: good morning michael (repeated on 5 lines)
# NOTE: argument order doesn't matter if we are explicit when sending in our arguments!
beCheerful(repeat=3, name="kb")		# output: good morning kb (repeated on 3 lines)

#--------------------------SORTING--------------------------
#---Python Swap
#- The swapping you've done in JavaScript probably looked something like this:
# // javascript code below!  
# var arr = [1,3,5,7];
# var temp = arr[0];
# arr[0] = arr[1];
# arr[1] = temp;

#- python code below-Python provides a one-liner way to swap:!
arr = [1,3,5,7]
arr[0], arr[1] = arr[1], arr[0]

#--- Python Bubble Sort
arr1=[1,5,3,2,0,8]
def bubble_sort(array):
    for j in range(len(array)-1):
        print("\n\n","-"*50,"Iteration",j)
        for i in range(len(array)-1-j):
            print("\n","*"*80,'\nindex',i,"value",array[i])
            print("\n","*"*80, "\ncomparing",array[i],array[i+1])
            if array[i]>array[i+1]:
                array[i],array[i+1]=array[i+1],array[i]
                print("swapped",array[i],array[i+1])
                print("array is now", array)
            else:
                print("no need to swap", array[i], array[i+1])
    return array
# bubble_sort(arr1)

#--------------------------TERNARY OPERATOR--------------------------
#---<result_if_true> if <condition> else <result_if_false>

#- traditional
if stacks >= 3:
    print('Coding Dojo')
else:
    print('You are not Coding Dojo!')
#- ternary
print('Coding Dojo' if stacks >= 3 else 'You are not Coding Dojo!')

#--------------------------LAMBDAS--------------------------
#--- In Python, anonymous functions are created with the lambda keyword. 
#- we defined the square() function that takes in one parameter (num), squares it and then returns it:
#- Functions where this implementation comes into play:
#- map()
#- reduce()
#- sort() - lambda is optional
#- filter() 

def square(num):
    x = num ** 2
    return x

#- rewrite this function as an anonymous (nameless) lambda function:
#- here is an anonymous (nameless) function that takes one argument, called num, and returns num**2.
lambda num: num ** 2

#--- A lambda could be:
#- an element in a list:
# create a new list, with a lambda as an element
my_list = ['test_string', 99, lambda x : x ** 2]
# access the value in the list
print(my_list[2]) # will print a lambda object stored in memory
# invoke the lambda function, passing in 5 as the argument
my_list[2](5)

#- passed to another function as a callback:
# define a function that takes one input that is a function
def invoker(callback):
    # invoke the input pass the argument 2
    print(callback(2))
invoker(lambda x: 2 * x)
invoker(lambda y: 5 + y)

#- stored in a variable:
add10 = lambda x: x + 10 # store lambda expression in a variable
add10(2)  # returns 12
add10(98) # returns 108

#- returned by another function:
def incrementor(num):
    start = num
    return lambda x: num + x

#- Lambdas & Other Functions
# create a list
my_arr = [1,2,3,4,5]
# define a function that squares values
def square(num):
    return num ** 2
# invoke map function
print(list(map(square, my_arr)))
# output: [1,4,9,16,25]

my_arr = [1,2,3,4,5]
print(list(map(lambda x: x ** 2, my_arr))) # invoke map, pass in a lambda as the first argument

#--------------------------SEQUENCES--------------------------
#--- Sequences are anything over which we can iterate sequentially, including lists, tuples, and strings.
#--- Slicing
my_tuple = (99,4,2,5,-3)
my_str = "sequoia"
print(my_list[:])
# output: [99,4,2,5,-3]
print(my_tuple[1:])
# output: (4,2,5,-3)
print(my_str[:3])
# output: "seq"
print(my_tuple[2:4])
# output: (2,5)
print(my_list, my_tuple, my_str)
# output: [99,4,2,5,-3] (99,4,2,5,-3) 'sequoia' -- note the original values have not changed

#- max(sequence) returns the largest value in the sequence
#- sum(sequence) returns the sum of all values in sequence
#- map(function, sequence) applies the function to every item in the sequence you pass in. Returns a list of the results.
#- min(sequence) returns the lowest value in a sequence.
#- sorted(sequence) returns a sorted list of the sequence's values
























#--------------------------PYTHON OOP--------------------------
#--------------------------CLASSES--------------------------

#-Here's the syntax for creating a class that we want to call User: 
class User:
    pass    # we'll fill this in shortly

#- And here's how we create a new instance of our class:
michael = User()
anna = User()

#--------------------------ATTRIBUTES--------------------------
#- attributes are characteristics of an object.
class User:		# declare a class and give it name User
    def __init__(self):
        self.name = "Michael"
        self.email = "michael@codingdojo.com"
        self.account_balance = 0

#-  The first parameter of every method within a class will be self, and the class's attribute names are also indicated by self.
#- self.<<attribute_name_of_your_choosing>>.
#- Then to instantiate a couple of new users:
guido = User()
monty = User()

#- If we want to access our instance's attributes, we can refer to them from our instances by name:
print(guido.name)	# output: Michael
print(monty.name)	# output: Michael

#- We can also set the values for our instance's attributes:
guido.name = "Guido"
monty.name = "Monty"

#- With the __init__ method's parameters, we indicate what needs to be provided (i.e. arguments) when the class is instantiated. (self is always passed in implicitly.)
class User:
    def __init__(self, username, email_address):# now our method has 2 parameters!
        self.name = username			# and we use the values passed in to set the name attribute
        self.email = email_address		# and the email attribute
        self.account_balance = 0		# the account balance is set to $0, so no need for a third parameter

#- Now when we want to create users, we must send in the 2 required arguments:
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
print(guido.name)	# output: Guido van Rossum
print(monty.name)	# output: Monty Python

#--------------------------METHODS--------------------------
#- Methods are just functions that belong to a class. 
guido.make_deposit(100)

#- To be able to call on this method, it needs to exist. Let's make it!
class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    	self.account_balance += amount	# the specific user's account increases by the amount of the value received

#-Now that our method is written, we can call it:
guido.make_deposit(100)
guido.make_deposit(200)
monty.make_deposit(50)
print(guido.account_balance)	# output: 300
print(monty.account_balance)	# output: 50

#---SELF
#- The self parameter includes all the information about the individual object that has called the method.
#- What's happening here? Because we are calling on the method from the instance, this is known as implicit passage of self. When we call on a method from an instance, that instance, along with all of its information (name, email, balance), is passed in as self.

#--------------------------ASSOCIATION BETWEEN CLASSES--------------------------
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)	# added this line

class User:
    def example_method(self):
        self.account.deposit(100)		# we can call the BankAccount instance's methods
    	print(self.account.balance)		# or access its attributes

#--------------------------MODULES AND PACKAGES--------------------------
#--- Modules
#- Modules are simply Python files with the .py extension which implement a set of functions. Modules are imported using the import command.
# import the library
import urllib.request
response = urllib.request.urlopen("http://www.codingdojo.com")
html = response.read()
print(html)
#- we used urllib.request as a variable to refer to our module and then we called the methods using dot notation.

#--- Creating Your Own Modules
#- To create a module, we first create a new .py file with the module name in the same directory as the file that will import the module. Then we import it using the import command and the Python file name (without the .py extension)

# modular_example/arithmetic.py
def add(x, y):
    return x + y
def multiply(x, y):
    return x * y
def subtract(x, y):
    return x - y
# import the arithmetic module into calculations.py and run the functions by doing this...

#modular_example/calculations.py
import arithmetic
print(arithmetic.add(5, 8))
print(arithmetic.subtract(10, 5))
print(arithmetic.multiply(12, 6))
# Note: make sure that the module and the file importing the module are in the same folder/directory.
# Exploring Built-In Modules
# Two very important functions come in handy when exploring modules in Python - the dir and help functions. We can look for which functions are implemented in each module by using the dir function:

#--- Packages
#- A module is a single file (or files) that are imported under one import. A package is a collection of modules in directories that give a package hierarchy.
from my_package.subdirectory import my_functions

#- Packages are namespaces which contain multiple packages and modules themselves. They are simply directories, but with a twist.
sample_project
     |_____ python_file.py
     |_____ my_modules
               |_____ __init__.py
               |_____ test_module.py
               |_____ another_module.py
               |_____ third_module.py

#--- Writing Packages
#- To use the module test_module, we can import it in two ways:
import my_modules.test_module
#-OR
from my_modules import test_module

#- __init__.py File
# You may have noticed the __init__.py file outlined in the structure above and wondered what it is. This file was required for all packages in Python 2.7; it would often be empty, but was required to indicate that the files in the folder were part of the package.
# In Python 3.3+, we only need this file if we need to customize what modules are available to anyone attempting to import the package
# if we didn't want another_module or third_module to be accessible for importing, we could override the __all__ variable, like so:

# sample_project/my_modules/__init__.py
__all__ = ["test_module"]

#--- Namespace - Namespace refers to which variables, functions, and classes are accessible to us at any given time during a program’s execution. 
print(locals())

#-We can use this conditional to prevent blocks of code from executing unless the file is being run directly. 
if __name__ == "__main__":
    product = Product([args])
    print(product)
    print(product.add_tax(0.18))

#--------------------------Unittest and Assertions--------------------------
#--- Python's unit testing framework, which was previously known as PyUnit, is included in the Python standard library. Let's get started with a simple "unit" and its tests. Create a new file:
#- test_even.py
# import the python testing framework
import unittest
# our "unit"
# this is what we are running our test on
def isEven(n):
    if n % 2 == 0:
       return True
    else:
       return False
# our "unit tests"
# initialized by creating a class that inherits from unittest.TestCase
class IsEvenTests(unittest.TestCase):
    # each method in this class is a test to be run
    def testTwo(self):
        self.assertEqual(isEven(2), True)
        # another way to write above is
        self.assertTrue(isEven(2))
    def testThree(self):
        self.assertEqual(isEven(3), False)
        # another way to write above is
        self.assertFalse(isEven(3))
    # any task you want run before any method above is executed, put them in the setUp method
    def setUp(self):
        # add the setUp tasks
        print("running setUp")
    # any task you want run after the tests are executed, put them in the tearDown method
    def tearDown(self):
        # add the tearDown tasks
        print("running tearDown tasks")
if __name__ == '__main__':
    unittest.main() # this runs our tests

#--- Running unittest
if __name__ == '__main__':
    unittest.main()
#- By including these two lines, we can run our test code by executing our python file. Running it with no options results in a simple output but running this file with the -v flag will give you the verbose output with information on each test that was run:

#--------------------------Multiple Arguments--------------------------
#---want to capture multiple arguments into a single parameter? Placing an asterisk before the name of the parameter after the "normal" parameters does just that. The asterisk is called a splat operator.
def varargs(arg1, *args):
    print("Got ", arg1, " and ", args)
varargs("one") 			# output: Got one and ()
varargs("one", "two") 	        # output: Got one and ('two',)
varargs("one", "two", "three")  # output: Got one and ('two', 'three')
#- the first argument arg1 is assigned to the first method parameter. ny and all remaining arguments passed in are in the args parameter, which appears to be a tuple (as indicated by the () syntax)!

#-  tuple is an iterable. That means if we want to access each of the arguments passed over individually, we can use a loop:
def varargs(arg1, *args):
    for a in args:
    	print(a)
varargs("one", "two", "three") # output: two, three (on separate lines)

#--------------------------LINKED LISTS--------------------------
#--- Linked List is another data structure that stores values in sequential order, but is more optimized for quick insertion and deletion. 
#--- Node-  is a class that, as described above, is going to have two attributes:
#- value - the actual value to be stored
#- next - a link to the node next to it in the list/next can be set to None
class SLNode:
    def __init__(self, value):
        self.value= value
        self.next= None

#- this first node is referred to as the head of the list.
class SList:
    def __init__(self):
        self.head= None

#- let's make an instance of our list:
my_list = SList()

#--------------------------INHERITANCE OOP--------------------------
#---inheritance, which is defining a new class based on another class. 
class CheckingAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
    	# code
    def withdraw(self, amount):
    	# code
    def write_check(self, amount):
    	# code
    def display_account_info(self):
    	# code

class RetirementAccount:
    def __init__(self, int_rate, is_roth, balance=0):
        self.int_rate = int_rate
        self.balance = balance
    	self.is_roth = is_roth
    def deposit(self, amount):
    	# code - assess tax if necessary
    def withdraw(self, amount):
    	# code - assess penalty if necessary
    def display_account_info(self):
    	# code
    
#- one parent class that holds the attributes and methods that are common between the new classes.
#- a child class will only contain what is unique to that class:
class CheckingAccount(BankAccount):
    pass    

 class RetirementAccount(BankAccount):
    pass
#- both the CheckingAccount and RetirementAccount classes both have all the attributes and functionality of the parent class

#--- Super
#- Here's what we want our RetirementAccount __init__ method to do
class RetirementAccount(BankAccount):
    def __init__(self, int_rate, is_roth, balance=0):
        self.int_rate = int_rate
        self.balance = balance
    	self.is_roth = is_roth  

#- Heres's what our parent BankAccount class __init__ method does
class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance

#- utilize the parent's functionality for this method, indicate the parent's methods by callingon it with the keyword super.
#- now you have the ability to call any of the parent's methods:
class RetirementAccount(BankAccount):
    def __init__(self, int_rate, is_roth, balance=0):
        super().__init__(int_rate,balance)
        self.is_roth= is_roth

class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate= int_rate
        self.balance= balance

#- first line in our RetirementAccount __init__ method allows the parent to manage the setting of int_rate and balance
#- The only line we need to add is to set the is_roth attribute, since this is unique to the RetirementAccount class.

#-add some logic to our withdraw method.
class RetirementAccount(BankAccount):
    def withdraw(self, amount, is_early):
        if is_early:
            amount= amount*1.10
        if (self.balance-amount) > 0:
            self.balance -= amount
        else:
            print("INSUFFICIENT FUNDS")
        return self

class BankAccount:
    def withdraw(self,amount):
        if(self.balance-amount)>0:
            self.balance -= amount
        else:
            print("INSUFFICIENT FUNDS")
        return self

#-  removing repetitiveness here by calling on the parent to do the part of the code that is the same:

class RetirementAccount(BankAccount):
    def withdraw(self,amount,is_ealry):
        if is_early:
            amount= amount * 1.10
        super().withdraw(amount)
        return self

class BankAccount:
    def withdraw(self,amount):
        if (self.balancr-amount) > 0:
            self.balance -= amount
        else:
            print("INSUFFICIENT FUNDS")
        return self

#--------------------------OVERRIDING & POLYMORPHISM OOP--------------------------
#--- Overriding
#- in the cases you want to override the function, replacing the functionality, define a function with the same name in the child class.
class Parent:
    def method_a(self):
        print("invoking PARENT method_a!")
class Child(Parent):
    def method_a(self):
        print("invoking CHILD method_a!")
dad = Parent()
son = Child()
dad.method_a()
son.method_a() #notice this overrides the Parent method!
#- The Child overrides this method from the parent by defining its own version.

#--- Polymorphism
#- Polymorphic behavior allows us to specify common methods in an "abstract" level and implement them in particular instances. 
# It is the process of using an operator or function in different ways for different data input.
 # We'll use the Person class to demonstrate polymorphism
# in which multiple classes inherit from the same class but behave in different ways
class Person:
    def pay_bill(self):
        raise NotImplementedError
# Millionaire inherits from Person
class Millionaire(Person):
    def pay_bill(self):
        print("Here you go! Keep the change!")
# Grad Student also inherits from the Person class
class GradStudent(Person):
    def pay_bill(self):
        print("Can I owe you ten bucks or do the dishes?")
#- xThis pattern is useful when you know that each subclass of a parent class must define a specific behavior in a method, 
#- and you don't want to define a default behavior in the parent class(hence the pure virtual implementation in the parent). 
