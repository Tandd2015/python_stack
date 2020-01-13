def make_dict(list1, list2): # beginning of function that gets passed two list variables when executed and returns a dictionary variable of the lists
    if len(list1) >= len(list2): # a condtionial to declare the variable to be sequenced in a particular order.
        new_dict = dict(zip(list1, list2)) # a variable with nested functions to turn the two lists into a dictionary creating key and value pairs out of each 
        print new_dict # print variable
    else:  #other half of a condtionial to declare the variable to be sequenced in a particular order.
        new_dict = dict(zip(list2, list1))  # a variable with nested functions to turn the two lists into a dictionary creating key and value pairs out of each
        print new_dict # print variable
    return new_dict # return variable
name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"] # variable that has a value of list of string elements
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]  # variable that has a value of list of string elements
make_dict(name, favorite_animal) # executing function and passing two list variables into the function