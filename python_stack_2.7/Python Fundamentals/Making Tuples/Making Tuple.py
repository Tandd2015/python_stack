def tupleMaker(dict): # beginning of function that has a dictionary variable passed through it when executed
    
    tupleHolder =[] # a variable with the value of an empty list
    
    for key, data in dict.items(): # foor loop to iterate through the key and value pairs in a dictionary
        #print key, data
        tuplele = ("{}".format(key), "{}".format(data)) # a variable that creates a tuple with nested functions to format strings with key and data variables
        tupleHolder.append(tuplele) # function to append a variable of a blank list with a variable of a tuple
    
    print tupleHolder # prints a variable

my_dict = { # variable that is a dictionary
   "Speros": "(555) 555-5555",
   "Michael": "(999) 999-9999",
   "Jay": "(777) 777-7777"
} 
tupleMaker(my_dict) # function call to pass a variable of a dictionary type when executed