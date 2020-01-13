def names(list): # beginning of a function that gets passed a variable that is a list
    
    for dict in list: # foor loop to iterate the list variable
        # print dict
        name = dict['first_name'] + ' ' + dict['last_name'] # a variable that concatenates two key values from the dictionary
        print name # print variable       

students = [ # a list of dictionaries as elements with key and value pairs
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]
names(students) # end of function passing list variable into execution statement

def names1(dict):# beginning of a function that gets passed a variable that is a dictionary 
    
    for value in dict: # foor loop to iterate the dictionary type variable
        counter = 0 # a variable to store times passed
        # print value 
        for val in dict[value]: # foor loop to iterate the values of each nesetd dictionary
            # print val
            counter += 1 # increasing the counter variable by 1 every loop
            #print counter
            first = val['first_name'].upper() # a variable with a function attached to it to change the casing of the charactars of the value called
            last = val['last_name'].upper() # a variable with a function attached to it to change the casing of the charactars of the value called
            name = first + ' ' + last # a variable that concatenates two key values from the dictionary
            strLength = len(first) + len(last) # a variable that has functions to count the length of each of the variables and then add the lengths together
            #print name
            #print strLength
            printOut = "{} - {} - {}".format(counter, name, strLength) # a variable to format a string every loop with updated variables and the values modified
            print printOut # print variable
            
users = { # a dictionary that has nested dictionaries
    'Students': [
        {'first_name': 'Michael', 'last_name': 'Jordan'},
        {'first_name': 'John', 'last_name': 'Rosales'},
        {'first_name': 'Mark', 'last_name': 'Guillen'},
        {'first_name': 'KB', 'last_name': 'Tonel'}
    ],
    'Instructors': [
        {'first_name': 'Michael', 'last_name': 'Choi'},
        {'first_name': 'Martin', 'last_name': 'Puryear'}
    ]
}           
names1(users) # end of function passing dictionary variable into execution statement