sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']
# list of variables and thier values to pass through the function

def filterType(viper): #function to get the type of a variable and then do something with the data depending on a boolean statement of what to actually do with it.
    snake = type(viper)
    if snake is int: # the first way to get the data type of a variable/ this is for the integers data types
        if viper >= 100:
            print "That's a big number!"
        else:
           print "That's a small number"
    elif snake is str: # the second time the first way to get the data type of a variable is used/ this is for string data types
        if viper >= 50:
            print "Long sentence"
        else:
            print "Short sentence"
    elif isinstance(viper, list): # the second most preferred way to get a data type pf a variable/ this is for list data types
        if len(viper) >= 10:
            print "Big list!"
        else:
            print "Short list!"
filterType(aL) #end of function 